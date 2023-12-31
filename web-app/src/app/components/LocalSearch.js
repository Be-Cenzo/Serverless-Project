'use client'

import { useState } from 'react';
import '../css/localsearch.css';
import map from '../img/map.png';

const LocalSearch = (props) => {
    const [value, setValue] = useState(50);
    console.log("kitammuort")
    console.log(props)

    const startSearching = () => {
        console.log("Setto il searching")
        props.setIsSearching(true);
        props.search(value, props.markers);
    }

    return(
        <div className="localsearch-container">
            <h4>Live Updates On Sensors</h4>
            <div className="localsearch-position">
                Choose a position on the map
                <div className='position-container'> 
                <button onClick={() => props.position()}>
                    <img className="button-icon" src={map.src} />
                </button>
                </div>
            </div>
            <div className="slider-container">
                Select the circle radius:
                <div className="slider-line">
                    <div style={{width:"80%"}}>
                        <input type="range" min="1" max="100" value={value} class="slider" onInput={(e) => {setValue(e.target.value)}} />
                    </div>
                    <div style={{width:"20%"}}>
                        {value}Km
                    </div>
                </div>
            </div>
            <div className="button-container">
                <button className="localsearch-button" onClick={() => {startSearching()}}>Get Live Data</button>
                <button className="localsearch-button" onClick={() => {props.setIsSearching(null) }}>Stop Live Data</button>
            </div>
        </div>
    );
}

export default LocalSearch;