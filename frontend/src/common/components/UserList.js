import React from "react";
import { useSelector } from "react-redux";

export default function UserList() {
    const users = useSelector( state => state.userReducer.users)

    return(<>
        {users.length === 0 && (<h1>지금은 등록된 회원이 없습니다.</h1>) }
        {users.length !== 0 && (<h1>{users.length} 명의 회원이 있습니다.</h1>)}
    </>)
}