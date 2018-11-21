import React, {Component} from 'react';

const Grade = (props) => {
    const students = props.students.map((student) => {
        return <a href="/signin/students/{student.id}" key={"student" + student.id}>{student.last_name} {student.first_name}</a>;
    })
    return (
  <article className="grade">
    <h3>{props.name}</h3>
    {students}
  </article>
    );
}
export default Grade;