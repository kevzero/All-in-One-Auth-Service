import React,{useState} from 'react';
import axios from 'axios';
export default function Login(){
  const [username,setUsername]=useState('');const [password,setPassword]=useState('');
  const login=async()=>{const res=await axios.post('http://localhost:8000/auth/login',{username,password});localStorage.setItem('token',res.data.access_token);window.location.href='/admin';}
  return(<div><h2>Login</h2><input placeholder='Username' onChange={e=>setUsername(e.target.value)}/><input type='password' placeholder='Password' onChange={e=>setPassword(e.target.value)}/><button onClick={login}>Login</button></div>);}