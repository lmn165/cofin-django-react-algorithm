import React from 'react'
import { Link } from 'react-router-dom'
import styled from 'styled-components'

const Navigation = () => (
<Nav class="navi">
    <NavList>
        <NavItem><Link to='/backtracking'>BackTracking</Link></NavItem>
        <NavItem><Link to='/bruteforce'>Brute Force</Link></NavItem>
        <NavItem><Link to='/divideconquer'>Divde Conquer</Link></NavItem>
        <NavItem><Link to='/dynamic'>Dynamic Programming</Link></NavItem>
        <NavItem><Link to='/greedy'>Greedy</Link></NavItem>
    </NavList>
    <NavList>
        <NavItem><Link to='/linear'>Linear</Link></NavItem>
        <NavItem><Link to='/math'>Math</Link></NavItem>
        <NavItem><Link to='/nonlinear'>NonLinear</Link></NavItem>
</NavList>
</Nav>
)

export default Navigation

const Nav = styled.div`
    width: 100%;
    height: 50px;
    border-bottom: 1px solid #d1d8e4;
`

const NavList = styled.ul`
    width: 1080px;
    display: flex;
    margin: 0 auto;
    padding: 0 auto;
`

const NavItem = styled.li`
    margin-left: 14px;
    margin-top: 5px;
    display: flex;
    font-size: 1.3vh;
`