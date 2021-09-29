import React from "react";
import { useSelector } from 'react-redux'

export default function TodoList() {
    const todos = useSelector( state => state.todoReducer.todos )

    return (
    <>
        {todos.length === 0 && (<h1>지금은 등록된 화면이 없습니다.</h1>) }
        {todos.length !== 0
            && (<h1>{todos.length} 개의 할일 목록이 있습니다.</h1>)}
    </>)
}