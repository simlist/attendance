import React, {Component} from 'react';

export default class SigninLine extends Component {

   constructor(props) {
     super(props);
     this.state = {};
     this.handleChange = this.handleChange.bind(this);
     this.first_name = this.props.location.state.student.first_name;
     this.last_name = this.props.location.state.student.last_name;
   }

   handleChange(e) {
      const id = e.target.id;
      this.setState({[id]: e.target.value});
   }

   render() {
      const datetime = new Date();
      const datestring = datetime.toDateString();
      return (
         <div className="formcontainer">
            <h2>{datestring} {this.first_name} {this.last_name}</h2>
            <form id="signinform">
               <input type="time" id="timein" value={this.state.timein} onChange={this.handleChange} />
               <input type="url" id="insignature" />
               <input type="time" id="timeout" />
               <input type="url" id="outsignature" />
            </form> 
         </div>
      )
   }
}