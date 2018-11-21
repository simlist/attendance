import React, {Component} from 'react';

import Grade from './grade.js';


class App extends Component {

    constructor(props) {
        super(props);
        this.state = {data: [], activeGrade: null};
        this.handleClick = this.handleClick.bind(this);
    }

    componentDidMount() {
        fetch('http://localhost:8000/signin/list.json')
        .then((response) => response.json())
        .then((data) => this.setState({data: data}));
    }

    handleClick(e) {
        e.preventDefault();
        this.setState({activeGrade: e.target.id})
    }

    render() {
        const grades = this.state.data.map((grade) => {
            const gradeInfo = parseInt(this.state.activeGrade)  === parseInt(grade.id)
                        && <Grade id={grade.id}
                        name={grade.name}
                        students={grade.students}>
                        </Grade>;
            return (
              <div className="grade" key={grade.name}>
                <a className="grade"
                    id={grade.id}
                    onClick={this.handleClick}
                    href="#"
                >
                {grade.name}
                </a>
                {gradeInfo}
             </div>
            );
        })

        return (
            <div className="grades-container">
                {grades}
            </div>
    );}
}
export default App;