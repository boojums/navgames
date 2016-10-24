
import moment from 'moment';

import React from 'react';
import ReactDOM from 'react-dom';

import { Grid, Row, Col } from 'react-bootstrap';
import { PageHeader } from 'react-bootstrap';
import bootstrapUtils from 'react-bootstrap';

import AgeGroup from './AgeGroup';
import ClassButtons from './ClassButtons';


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


module.exports = React.createClass({
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
