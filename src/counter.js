import React,{Component} from 'react';
import './index.css';
import logo from './image/safeline_logo1.png';
import screenshot1 from './image/login_screen.jpg';
import downbutton from './image/button.png';
import logo2 from './image/safeline_logo.png';
import { Container, Row, Col } from 'reactstrap';
import CountUp from 'countup.js'

export default class Counter extends Component {

    constructor(props){
        super(props);
        this.clicked = this.clicked.bind(this);
        this.state = {change:true}        
        
        this.number = 0;
    }

    clicked(){
        console.log("test");
        this.numAnim = new CountUp("counter1", 1, 11, 0, 7);
        if (!this.numAnim.error) {
            this.numAnim.start();
        } else {
            console.error(this.numAnim.error);
        }

        this.numAnim1 = new CountUp("counter2", 1, 7000000, 0, 4);
        if (!this.numAnim1.error) {
            this.numAnim1.start();
        } else {
            console.error(this.numAnim1.error);
        }

        this.numAnim2 = new CountUp("counter3", 1, 19, 0, 7);
        if (!this.numAnim2.error) {
            this.numAnim2.start();
        } else {
            console.error(this.numAnim2.error);

        }
        this.setState({
            change:true
        })
    }
    
    render() {
        return (
            <Container id='container'>
                <Row id='background'>
                    <img id='logo' src={logo}></img>
                    <h1 id='learnmore'>learn more!</h1>
                    <a id='downbutton' href='#intro1' onClick={this.clicked} ><img id='downbutton' src={downbutton}></img></a>
                </Row>
                <Row>
                    <h1 id='intro1'>we are</h1>
                    <h1 id='intro2'>safeline</h1>
                    <div className='dash'></div>
                </Row>
                <Row style={{display:"flex", textAlign:"center", margin:'1vh'}}>
                    <Col style={{width:"33.3%", paddingLeft:'10%', paddingRight:'10%', paddingBottom:'1%', paddingTop:'2%'}}>
                        <div id='counter1'></div>
                        every 11 seconds, an older adult is treated in the emergency room for a fall
                    </Col>
                    <Col style={{width:"33.3%", paddingLeft:'10%', paddingRight:'10%', paddingBottom:'1%', paddingTop:'2%'}}>
                    <   div id='counter2'></div>
                        In 2014, older Americans experienced 29 million falls, resulting in 7 million injuries
                    </Col>
                    <Col style={{width:"33.3%", paddingLeft:'10%', paddingRight:'10%', paddingBottom:'1%', paddingTop:'2%'}}>
                        <div id='counter3'></div>
                        Every 19 minutes, an older adult dies from a fall
                    </Col>
                </Row>
                <Row>
                    <h1 id="mediumwriting">keep your community <blue>safe</blue></h1>
                    <h1 id="smallwriting">we are a medical alert system powered by AI fall-detection that <red>immediately</red> notifies your connections - designed to protect senior citizens and all members in home health emergencies</h1>
                </Row>
                <Row style={{display:"flex", textAlign:"center", margin:'5vh'}}>
                    <Col style={{width:"50%", margin:"0%", paddingLeft:'18%', paddingRight:'10%', paddingBottom:'1%', paddingTop:'8%'}}>
                        <img src={screenshot1}></img>
                    </Col>
                    <Col style={{width:"50%", margin:"0%", paddingTop:'25%', paddingRight:'20%'}}>
                        <h1 id='info'><red>login</red></h1>
                        <h1 id='info'> and <blue2>sign-up</blue2></h1> 
                        <h1 id='info'>in seconds</h1>
                    </Col>
                </Row>
                <Row style={{display:"flex", textAlign:"center", margin:'5vh'}}>
                    <Col style={{width:"50%", margin:"0%", paddingTop:'18%', paddingLeft:'20%'}}>
                        <h1 id='info'>access your</h1>
                        <h1 id='info'><red>community</red></h1> 
                        <h1 id='info'>easily</h1>
                    </Col>
                    <Col style={{width:"50%", margin:"0%", paddingLeft:'10%', paddingRight:'18%', paddingBottom:'1%', paddingTop:'1%'}}>
                        <img src={screenshot1}></img>
                    </Col>
                </Row>
                <Row>
                    <img id='logo2' src={logo2}></img>
                </Row>
                <Row>
                    <h1 id='smallwriting'>created by brandon khong, bryon tjanaka, cody enokida, and meta novitia</h1>
                </Row>
            </Container>
        );
    }
}