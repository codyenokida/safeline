import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import logo from './image/safeline_logo.gif';
import { Container, Row, Col } from 'reactstrap';
// import "bootstrap/dist/css/bootstrap.css"

ReactDOM.render(
    <Container>
        <Row id='background'>
            <img id='logo' src={logo}></img>
            <h1 id='learnmore'>learn more!</h1>
        </Row>
        <Row>
            <h1 id='intro1'>we are</h1>
            <h1 id='intro2'>safeline</h1>
            <div className='dash'></div>
        </Row>
        <Row style={{display:"flex", textAlign:"center", margin:'5vh'}}>
            <Col style={{width:"33.3%", padding:'10%'}}>every 11 seconds, an older adult is treated in the emergency room for a fall</Col>
            <Col style={{width:"33.3%", padding:'10%'}}>In 2014, older Americans experienced 29 million falls, resulting in 7 million injuries</Col>
            <Col style={{width:"33.3%", padding:'10%'}}>Every 19 minutes, an older adult dies from a fall</Col>
        </Row>
    </Container>,
    document.getElementById('root')
);
