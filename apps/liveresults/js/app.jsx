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

- include css (bootstrap)
*/

import React from 'react';
import ReactDOM from 'react-dom';

import Event from './components/Event';

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
