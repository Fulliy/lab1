import './App.css'
import { useState } from "react";
import ProductCard from './ProductCard';

function App() {
    return (
  <div>
    <h1>Овощи</h1>
    <ProductCard name="авокадо" price="100" image="https://avatars.mds.yandex.net/i?id=b423804ea65812a8472dd55128df9bb2873e0cd9-11918841-images-thumbs&n=13" />
  </div>
  );
}

export default App;

