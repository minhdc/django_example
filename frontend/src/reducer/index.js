import { combieReducers, combineReducers } from 'redux';
import * as actionType from '../actions/types';

const tokenInitialState = null;
const token = (state = tokenInitialState,acion) => {
    switch(action.type){
        case actionType.SET_TOKEN:
            return action.data;
        default:
            return state;
    }
}

const appReducer = combineReducers({
    token,
})

const rootReducer = (state, action) => {
    return appReducer(state, action);
}

export default rootReducer;