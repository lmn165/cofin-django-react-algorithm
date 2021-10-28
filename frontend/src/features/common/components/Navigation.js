import React from 'react'
import { Link } from 'react-router-dom'

export default function Navigation (){
    return (<>
        <div class="navi">
            <ul>
                <li><Link to='/add'>add</Link></li>
                <li><Link to='/detail'>detail</Link></li>
                <li><Link to='/list'>list</Link></li>
                <li><Link to='/login'>login</Link></li>
                <li><Link to='/modify'>modify</Link></li>
                <li><Link to='/remove'>remove</Link></li>
            </ul>
        </div>
</>)
}
