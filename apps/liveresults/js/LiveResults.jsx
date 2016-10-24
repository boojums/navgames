/* TODO:
- handle status not OK (e.g. MSP)
- make runner red if dsq
- map statuses to something textual
- make reponsive (buttons in dropdown?)
- parser selection (iofxml vs. other,evt json)
- refactor results/lists names
- one function for person parsing?
- grab event info from external source?
- use id instead of name for class id+
- change notification
- tabs to show just starts, just finishes, etc.
- better handling of default/different course lists
- search bar?
- autorefresh button
- use ES6 let/const
- use ES6 arrow functions

- split components into files
- extend base.html, etc. 
- include css (bootstrap)
*/

import moment from 'moment';

import React from 'react';
import ReactDOM from 'react-dom';

import { Table, ButtonGroup, Button } from 'react-bootstrap';
import { Panel, Grid, Row, Col } from 'react-bootstrap';
import { PageHeader, ButtonToolbar } from 'react-bootstrap';
import bootstrapUtils from 'react-bootstrap';

//const bootstrapUtils = ReactBootstrap.utils.bootstrapUtils;

//var results = data.results;
//var startlist = data.startlist;
//bootstrapUtils.addStyle(Button, 'custom');

/* Standard US A-meet classes */
/* All this stuff should be served as JSON, accessible from a RESTful API */ 
/* Could test wtih: 
http://www.nephridium-labs.com/blog/setting-up-a-rest-service-within-minutes/
*/
const classColors = {"F-10": "black", "M-10": "black", "F-12": "black", "M-12": "black", "F-14": "yellow", "M-14": "yellow", "F-16": "orange", "M-16": "orange", "F-18": "brown", "F-20": "green", "F-21+": "red", "F35+": "green", "F40+": "green", "F45+": "green", "F50+": "green", "F55+": "brown", "F60+": "brown", "F65+": "brown", "F70+": "brown", "F75+": "brown", "F80+": "brown", "F85+": "brown", "M-18": "green", "M-20": "red", "M-21+": "blue", "M35+": "red", "M40+": "red", "M45+": "red", "M50+": "green", "M55+": "brown", "M60+": "brown", "M65+": "brown", "M70+": "brown", "M75+": "brown", "M80+": "brown", "M85+": "brown",};

const fClassOrder = ["F-10", "F-12", "F-14", "F-16", "F-18", "F-20", "F-21+", "F35+", "F40+", "F45+", "F50+", "F55+", "F60+", "F65+", "F70+", "F75+", "F80+", "F85+"];

const mClassOrder = ["M-10", "M-12", "M-14", "M-16", "M-18", "M-20", "M-21+", "M35+", "M40+", "M45+", "M50+", "M55+", "M60+", "M65+", "M70+", "M75+", "M80+", "M85+"];

const otherClassOrder = ["Rec White", "F-White", "M-White", "F-Yellow", "M-Yellow", "F-Orange", "M-Orange", "F-Brown", "M-Brown", "F-Green", "M-Green", "F-Red", "M-Red"];


let parseResultPerson = function(personResult) {
  let person = {
    last: $(personResult).find("Person > Name > Family").text(),
    first: $(personResult).find("Person > Name > Given").text(),
    bib: $(personResult).find("BibNumber").text(),
    sex: $(personResult).find("Person").attr("sex"),
    club: $(personResult).find('Organisation > Name').text(),
    time: $(personResult).find("Time").text(),
    starttime: $(personResult).find("StartTime").text(),
    finishtime: $(personResult).find("FinishTime").text(),
    timebehind: $(personResult).find("TimeBehind").text(),
    position: $(personResult).find("Position").text(),
    status: $(personResult).find("Status").text()
  }
  return person;
}

let parseStartPerson = function(personStart) {
  let person = {
    last: $(personStart).find("Person > Name > Family").text(),
    first: $(personStart).find("Person > Name > Given").text(),
    bib: $(personStart).find("BibNumber").text(),
    sex: $(personStart).find("Person").attr("sex"),
    club: $(personStart).find('Organisation > Name').text(),
    starttime: $(personStart).find("StartTime").text(),
    finishtime: null,
    time: null,
    timebehind: null,
    position: null,
    status: null
  }
  return person;
}
let parseResults = function(results) {
  //var xmlDoc = $.parseXML( results );
  let $xml = $(results);
  let data = {
    eventName: $xml.find("Event").find("Name").text(),
  };
  
  let classes = $xml.find("ClassResult");
  data.classes = [];
  classes.each(function() {
    let results = [];
    $(this).find("PersonResult").each(function() {
      results.push(parseResultPerson($(this)));
    });
    var classResult = {
      name: $(this).find("Class > Name").text(),
      courseLength: $(this).find("Course > Length").text(),
      results: results
    }
    data.classes.push(classResult);
  });
  return data;
}

/* Returns an object with the following structure
  name: the name of the event
  classes: array of...
    classinfo:
      name: the name of the class (e.g. M-14)
      courseLength: length of the course in m
      startList: array of persons objects
*/
let parseStartlist = function(xmldata) {
  //var xmlDoc = $.parseXML( results );
  let $xml = $(xmldata);  
  let classes = $xml.find("ClassStart");
  let data = {
    eventName: $xml.find("Event").find("Name").text(),
  };
  data.classes=[]
  classes.each(function() {
    let startlist = [];
    $(this).find("PersonStart").each(function() {
      startlist.push(parseStartPerson($(this)));
    });
    let classInfo = {
      name: $(this).find("Class > Name").text(),
      courseLength: $(this).find("Course > Length").text(),
      startList: startlist
    }
    data.classes.push(classInfo);
  });
  return data;
}

/* Returns an array of classInfos where each person is included, whether
   as a result or a start.*/
let mergelists = function(startlist, resultslist) {
  let merged = [];
  /* For each class in the start list see if there are results for it */
  startlist.map(function(startclass) {
    let classname = startclass.name;
    let resultclass = resultslist.find(function(clas) {
      return clas.name == classname;
    });
    /* Set the metadata for the new classInfo object */
    let mergedclass = {name: classname, length: startclass.courseLength}
    
    /* Add all the runners from the resultslist and the rest from the startlist. */
    if (resultclass == null) {
      mergedclass['runners'] = startclass.startList;
    } else {
      let runners = resultclass.results;
      startclass.startList.map(function(personstart) {
        let personresult = runners.find(function(personresult) {
          return personresult.bib == personstart.bib;
        });
        if (personresult == null) {
          runners.push(personstart);
        }
      });
      mergedclass['runners'] = runners;
    }
    merged.push(mergedclass);
  });
  return merged;
}

let sortEveryone = function(a, b) {
  if (a.status != 'OK' && b.status == 'OK') {
    return 1;
  } else if (a.status == 'OK' && b.status != 'OK') {
    return -1;
  } else if (a.time < 0 && b.time > 0) {
    return 1;
  } else if (b.time < 0 && a.time > 0) {
    return -1;
  } else if (a.time < 0 && b.time < 0) {
    return (b.time - a.time)
  } else {
    return (a.time - b.time);
  }
}

let Event = React.createClass({
  updateTimes: function() {
    let now = moment();
    let simnow = moment({year: 2016, month: 8, day: 23, hour: 14, minute: now.minutes(), seconds: now.seconds()});
    this.setState({now: simnow});
  },
  getResults: function() {
      return $.get(this.props.resultlisturl, function(data) {
        let results = parseResults(data);
        this.resultslist = results.classes;
        }.bind(this))   
  },
  getStartlist: function() {
     return $.get(this.props.startlisturl, function(data) {
        let startlist = parseStartlist(data);
        this.startlist = startlist.classes;
        }.bind(this))
  },
  fetchAll: function() {
    $.when(
      this.getResults(),
      this.getStartlist()
    ).then(function() {
       let merged = mergelists(this.startlist, this.resultslist);
       this.setState({merged: merged});
    }.bind(this));
  },
  handleClassClick(id) {
    this.setState({selectedClass: id});
  },
  getInitialState: function() {
    return {merged: [], now: null, selectedClass: null};
  },
  componentDidMount: function() {
    this.fetchAll();
    this.fetchInterval = setInterval(this.fetchAll, this.props.pollInterval);
    this.updateInterval = setInterval(this.updateTimes, 1000);
  },
  componentWillUnmount: function() {
    clearInterval(this.fetchInterval);
    clearInterval(this.updateInterval);
  },
  render: function() {
    if (!this.state.merged) {return null;}
    let classList = this.state.merged.map(function(data) {
      return data.name;
    });
    let now = this.state.now;
    let resultsClasses = this.state.merged.filter(function(data) {
      return data.name == this.state.selectedClass;
    }, this).map(function(data) {
      return (
        <AgeGroup data={data} now={now} key={data.name}></AgeGroup>
      );
    });
    
    if (resultsClasses.length == 0) {
      resultsClasses = <h3>{"Select a class to view live results."}</h3>
    }
    
    return (
      <div>
        <Grid><Row>
        <PageHeader>{this.props.name}</PageHeader>
        <Col md={12}>
          <ClassButtons data={classList} handleClick={this.handleClassClick}/>
        </Col>
        <Col md={12}>    
          <div style={{marginTop: '10px'}}>
            {resultsClasses}
          </div>
        </Col>
        </Row></Grid>
      </div>
    )
  }
})

/* Return a zero-padded number string. */
let zeroPad = function(number) {
  return number < 10 ? "0" + number : number.toString();
}

/* Return [hh]:MM:ss string for an elapsed time in seconds. */
let secondsToString = function(seconds) {
  let neg = (seconds < 0) ? '-' : '';
  seconds = Math.abs(seconds);
  let hours = Math.floor(seconds / 3600);
  seconds = seconds - (hours * 3600);
  let minutes = zeroPad(Math.floor(seconds / 60));
  seconds = zeroPad(Math.floor(seconds - (minutes * 60)));
  
  hours = hours > 0 ? hours.toString() + ":" : "";
  return neg + hours + minutes + ":" +  seconds;
}

let ClassButtons = React.createClass({
  handleClassClick: function(e) {
    this.props.handleClick(e.target.id);
  },
  handleGroupClick: function(e) {
    this.setState({group: e.target.id});
  },
  getInitialState: function() {
    return {group: null}
  },
  filterClassNames: function(name) {
      return this.props.data.indexOf(name) > 0;
  },
  mapClassNames: function(name) {
    let style = {color: classColors[name]};
    return (
        <ButtonGroup key={name}><Button bsSize="sm" 
          onClick={this.handleClassClick} style={style} key={name} id={name}>{name}</Button>            </ButtonGroup>)
  },
  mapGroupNames: function(name) {
      return (
        <ButtonGroup key={name}>
          <Button bsSize="sm" 
            onClick={this.handleGroupClick} key={name} id={name}>{name}
          </Button>            
        </ButtonGroup>)
  },  
  selectClassOrder: function() {
    if (this.state.group == "F-classes") return fClassOrder;
    if (this.state.group == "M-classes") return mClassOrder;
    if (this.state.group == "Other classes") return otherClassOrder;
    if (this.state.group == null) return null;
    console.log(this.state.group);
  },
  render: function() {
    let classOrder = this.selectClassOrder();
    let displayClasses = null;
    if (classOrder != null) {
      displayClasses = classOrder.filter(this.filterClassNames).map(this.mapClassNames);
    }
    //var mclasses = mClassOrder.filter(this.filterClassNames).map(this.mapClassNames);
    //var fclasses = fClassOrder.filter(this.filterClassNames).map(this.mapClassNames);
    //var otherClasses = otherClassOrder.filter(this.filterClassNames).map(this.mapClassNames);
    let groupButtons = ["F-classes", "M-classes", "Other classes"].map(this.mapGroupNames);
    return (
      <div>
      <Col>
        <ButtonGroup>
          {groupButtons}
        </ButtonGroup>
       <div style={{marginTop:'10px'}}>
       <ButtonGroup>
          {displayClasses}
        </ButtonGroup></div>       
      </Col>
      </div>
    );
  }
});

let AgeGroup = React.createClass({
  render: function() {
    let lengthkm = this.props.data.length / 1000;
    let people = this.props.data.runners.map(function(person) {
      let time, timebehind, status, minperkm;
      if (person.finishtime) {
        time = parseInt(person.time);      
        timebehind = secondsToString(person.timebehind);
        minperkm = secondsToString(person.time / lengthkm);
        status = person.status;
      } else {
        time = this.props.now.diff(moment(person.starttime), 'seconds');
        status = time > 0 ? 'On course' : 'Not started';
      };
      return ({
        position: person.position,
        bib: person.bib,
        first: person.first,
        last: person.last,
        club: person.club,
        time: time,
        timebehind: timebehind,
        minperkm: minperkm,
        status: status
      });
    }, this);

    people = people.sort(sortEveryone);
    
    people = people.map(function(person) {
        let style;
        if (person.status == 'On course' || person.status == 'Not started') { 
          style = {color: 'green'};      
        }
      return (
        // TODO: should be person.bib
        <tr style={style} key={person.bib}>
          <td>{person.position ? person.position : person.status}</td>
          <td>{person.first} {person.last}</td>
          <td>{person.club}</td>
          <td>{secondsToString(person.time)}</td>
          <td>{person.timebehind}</td>
          <td>{person.minperkm}</td>
        </tr>
      );
    });
    
    return (
      <Grid><Row>
      <Col>
        <Panel collapsible defaultExpanded header={this.props.data.name}>
          <Table striped hover responsive fill>
          <thead><tr>
            <th>Place</th>
            <th>Name</th>
            <th>Club</th>
            <th>Time</th>
            <th>Time behind</th>
            <th>Min/km</th>
          </tr></thead>
          <tbody>
            {people}
          </tbody>
        </Table>
        </Panel>
        </Col></Row></Grid>
     );
  }
});

ReactDOM.render(
    <div>
      <Event name={"NAOC 2016 - Middle"}
            startlisturl={"http://crossorigin.me/http://www.orienteering-live.com/middle/xml/startlist.xml"}   
            resultlisturl={"http://crossorigin.me/http://www.orienteering-live.com/middle/xml/results.xml"}
            pollInterval={100000} 
      />
    </div>,
  document.getElementById("app")
);
