import './App.css';
import React, { useState } from "react";
import { getNews, getCategory, getFiveCategory } from './service/fetch';

const newMsg = (<h2>Carregando....</h2>)

function App() {
  const [news, setNews] = useState(0)
  const [noticias, setNoticias] = useState([])
  const [msg, setMsg] = useState('')
  const [title, setTitle] = useState('')
  const [newTitle, setNewTitle] = useState([])
  const [carregar, setCarregar] = useState(false)
  const [top, setTop] = useState([])
  console.log(news);
  const handleClick = async () => {
    if (news === 0) {
      alert('Please, select a message')
    } else {
      const response = {
        method: 'GET',
        headers: {
          'Access-Control-Allow-Credentials': 'true',
          'Access-Control-Allow-Origin': '*',
          'Access-Control-Allow-Methods': 'GET,OPTIONS,PATCH,DELETE,POST,PUT',
          'Access-Control-Allow-Headers': 'X-CSRF-Token, X-Requested-With, Accept, Accept-Version, Content-Length, Content-MD5, Content-Type, Date, X-Api-Version, Authorization'
        },
      }
      setTop([])
      setNewTitle([])
      setMsg(newMsg)
      setCarregar(true)
      const result = await getNews(Number(news), response)
      if (result.length > 0) {
        setNoticias(result)
        setCarregar(false)
      }
    }
    
  }

  const handleTitle = async () => {
    if (title.length === 0) {
      alert("No category selected")
    } else {
      const response = {
        method: 'GET',
        headers: {
          'Access-Control-Allow-Credentials': 'true',
          'Access-Control-Allow-Origin': '*',
          'Access-Control-Allow-Methods': 'GET,OPTIONS,PATCH,DELETE,POST,PUT',
          'Access-Control-Allow-Headers': 'X-CSRF-Token, X-Requested-With, Accept, Accept-Version, Content-Length, Content-MD5, Content-Type, Date, X-Api-Version, Authorization'
        },
      }
      setNoticias([])
      setTop([])
      setMsg(newMsg)
      setCarregar(true)
      const result = await getCategory(title, response)
      if (result.length > 0) {
        setNewTitle(result)
        setCarregar(false)
      }
    }

  }

  const handleFiveCategory = async () => {
    const response = {
      method: 'GET',
      headers: {
        'Access-Control-Allow-Credentials': 'true',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET,OPTIONS,PATCH,DELETE,POST,PUT',
        'Access-Control-Allow-Headers': 'X-CSRF-Token, X-Requested-With, Accept, Accept-Version, Content-Length, Content-MD5, Content-Type, Date, X-Api-Version, Authorization'
      },
    }
    setNoticias([])
    setNewTitle([])
    setMsg(newMsg)
    setCarregar(true)
    const result = await getFiveCategory(response)
    if (result.length > 0) {
      setTop(result)
      setCarregar(false)
    }
  }

 
  const result = noticias.map((i, index) => (
    <div key={index} className='div-news'>
      <li>{i.category}</li>
      <li>{i.title}</li>
      <li>{i.writer}</li>
      <li className='url'><a href={i.url}><h3>Link</h3></a></li>
      <li className='summary'>{i.summary}</li>
    </div>
  ))

  const data = newTitle.map((i, index) => (
    <div key={index} className='div-data'>
      <li>{i[0]}</li>
      <li className='url'><a href={i[1]}><h3>Link</h3></a></li>
    </div>
  ))

  const five = top.map((i, index) => (
    <div key={index} className='div-top'>
      <li>{i}</li>
    </div>
  ))
  return (
    <div className="App">
      <header className="App-header">
        <h3>Tech-news Project!</h3>
        <div className='article'>
          <input type='number' placeholder='Digite quantas noticias' onChange={(e) => setNews(e.target.value)} />
          <button type='button' onClick={handleClick}>news</button>
          <input
            type='text'
            placeholder='Digite a categoria'
            className='category-select'
            onChange={(e) => setTitle(e.target.value)}
          />
          <button type='button' onClick={handleTitle}>category</button>
          <button type='button' onClick={handleFiveCategory} className='top-five'>top-5</button>
        </div>
        {carregar ? msg : <ul className='result'>
          {result}
        </ul>}
        {carregar ? msg : <ul className='result-data'>{data}</ul>}
        {carregar ? msg : <ul className='result-data'>{five}</ul>}

      </header>
    </div>
  );
}

export default App;
