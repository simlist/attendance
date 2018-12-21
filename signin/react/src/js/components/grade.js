import React, {Component} from 'react';
import {Link} from 'react-router-dom';

const Grade = (props) => {
    const students = props.students.map((student) => {
        return <Link to={{pathname: "/signin/student/", state: {student: student} }}key={"student" + student.id}>{student.last_name} {student.first_name}</Link>;
    })
    return (
  <article className="grade">
    <h3>{props.name}</h3>
    {students}
  </article>
    );
}
export default Grade;