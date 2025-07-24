import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Login from './pages/Login';
import Register from './pages/Register';
import AdminPanel from './pages/AdminPanel';
export default function App(){
  return (<Router><Routes><Route path='/' element={<Login/>}/><Route path='/register' element={<Register/>}/><Route path='/admin' element={<AdminPanel/>}/></Routes></Router>);}