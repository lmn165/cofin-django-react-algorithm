import React from "react";
import { useSelector, useDispatch } from 'react-redux'
import { toggleTodoAction, deleteTodoAction } from "reducers/todo.reducer";

export default function TodoList() {
    const todos = useSelector( state => state.todoReducer.todos )
    const dispatch = useDispatch()
    const toggleTodo = id => dispatch(toggleTodoAction(id))
    const deleteTodo = id => dispatch(deleteTodoAction(id))
    return (
    <>
        {todos.length === 0 && (<h1>지금은 등록된 화면이 없습니다.</h1>) }
        {todos.length !== 0 && (<h1>{todos.length} 개의 할일 목록이 있습니다.</h1>)}

        {todos.length !== 0 && todos.map(
            todo => (<div key={todo.id}>
                <input type='checkbox' checked={todo.complete} onChange={toggleTodo.bind(null, todo.id)}/>
                {todo.complete ?
                <span style={{textDecoration: 'line-through'}}>{todo.name}</span>
                : <span>{todo.name}</span>}
                <button onClick={deleteTodo.bind(null, todo.id)}>X</button>
            </div>)
        )}
    </>)
}