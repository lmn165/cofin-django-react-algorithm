const initialState = {todos:[], todo:{}}
export const addTodoAction = todo => ({type: "ADD_TODO", payload: todo})
export const toggleTodoAction = todoid => ({type: "TOGGLE_TODO", payload: todoid})
export const deleteTodoAction = todoid => ({type: "DELETE_TODO", payload: todoid})
const todoReducer = (state = initialState, action) => {
    switch(action.type){
        case 'ADD_TODO': return {...state, todos:[...state.todos, action.payload]}
        case 'TOGGLE_TODO': return {...state, todos:state.todos.map(todo => (todo.id === action.payload)
                                                                    ? {...todo, complete: !todo.complete} : todo)}
        case 'DELETE_TODO': return {...state, todos:state.todos.filter(todo => todo.id != action.payload)}
        default : return state
    }
}
export default todoReducer