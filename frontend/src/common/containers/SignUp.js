import React from "react";
import styled from 'styled-components'
import { UserJoin, UserList } from 'common'

export default function SignUp() {
    return(
        <TodoDiv>
            <UserJoin/>
            <UserList/>
        </TodoDiv>
    )
}

const TodoDiv = styled.div` text-align: center; `