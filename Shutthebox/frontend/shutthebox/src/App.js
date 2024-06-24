import React, {useState, useEffect} from 'react'
import Dice from './components/dice.js'
import Boxes from './components/boxes.js'


function App() {
  const [data, setData] = useState([{}])

  useEffect(() => {
    fetch("/members").then(
      res => res.json()
    ).then(
      data => {
        setData(data)
        console.log(data)
      }
    )
  }, [])

  const sumbitDice = async () => {
    const myData = <Dice></Dice>
  }

  return (
    <div className='App'>
      <Boxes></Boxes>
      <Dice></Dice>
      <button onClick={sumbitDice}> Submit</button>
      {(typeof data.members === 'undefined') ? (
        <p>Loading...</p>
      ) : (
        data.members.map((member, i) => (
          <p key={i}>{member}</p>
        ))
      )}
    </div>
  )
}

export default App

