import moment from 'moment';

import React from 'react';
import ReactDOM from 'react-dom';

import { ButtonGroup, Button } from 'react-bootstrap';
import { Col } from 'react-bootstrap';

/* Standard US A-meet classes */
/* All this stuff should be served as JSON, accessible from a RESTful API */ 
/* Could test wtih: 
http://www.nephridium-labs.com/blog/setting-up-a-rest-service-within-minutes/
*/
const classColors = {}
//const classColors = {"F-10": "black", "M-10": "black", "F-12": "black", "M-12": "black", "F-14": "yellow", "M-14": "yellow", "F-16": "orange", "M-16": "orange", "F-18": "brown", "F-20": "green", "F-21+": "red", "F35+": "green", "F40+": "green", "F45+": "green", "F50+": "green", "F55+": "brown", "F60+": "brown", "F65+": "brown", "F70+": "brown", "F75+": "brown", "F80+": "brown", "F85+": "brown", "M-18": "green", "M-20": "red", "M-21+": "blue", "M35+": "red", "M40+": "red", "M45+": "red", "M50+": "green", "M55+": "brown", "M60+": "brown", "M65+": "brown", "M70+": "brown", "M75+": "brown", "M80+": "brown", "M85+": "brown",};

const fClassOrder = ["F-10", "F-12", "F-14", "F-16", "F-18", "F-20", "F-21+", "F35+", "F40+", "F45+", "F50+", "F55+", "F60+", "F65+", "F70+", "F75+", "F80+", "F85+"];

const mClassOrder = ["M-10", "M-12", "M-14", "M-16", "M-18", "M-20", "M-21+", "M35+", "M40+", "M45+", "M50+", "M55+", "M60+", "M65+", "M70+", "M75+", "M80+", "M85+"];

const otherClassOrder = ["Rec White", "F-White", "M-White", "F-Yellow", "M-Yellow", "F-Orange", "M-Orange", "F-Brown", "M-Brown", "F-Green", "M-Green", "F-Red", "M-Red"];



module.exports = React.createClass({
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
