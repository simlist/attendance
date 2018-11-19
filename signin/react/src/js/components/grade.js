import React, {Component} from React;

export default grade = (props) => {
    students = props.students.map((student) => {
        return <a href="/signin/students/{student.id}" key={student.id}>{student.last_name} {student.first_name}</a>
    })
    return (
  <article className="grade">
    <h3>{props.grade.name}</h3>
    {students}
  </article>
    );
}