import React, {Component} from 'react';


class App extends Component {

    constructor(props) {
        super(props);
        this.state = {data: []};
    }

    componentDidMount() {
        fetch('http://localhost:8000/signin/list.json')
        .then((response) => response.json())
        .then((data) => this.setState({data: data}));
    }

    render() {
        const grades = this.state.data.map((grade) => <a className="grade" id={grade.name} key={grade.name}>{grade.name}</a>)
        return (
        <div className="grades-container">
          {grades}
        </div>
    );}
}
export default App;