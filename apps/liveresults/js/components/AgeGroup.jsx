import React from 'react';
import ReactDOM from 'react-dom';

import moment from 'moment';

import { Table, ButtonGroup, Button } from 'react-bootstrap';
import { Panel, Grid, Row, Col } from 'react-bootstrap';
import { PageHeader, ButtonToolbar } from 'react-bootstrap';
import bootstrapUtils from 'react-bootstrap';

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

/* Return a zero-padded number string. */
let zeroPad = function(number) {
  return number < 10 ? "0" + number : number.toString();
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

module.exports = React.createClass({
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