import { useState } from "react";

function ProductCard(props) {
    const [count, setCount] = useState(0);

    function handleClick() {
        setCount(count + 1);
    }

    return (
        <div>
        <p>корзина: {count}</p>
        <p>Название: {props.name}</p>
        <p>Цена: {props.price}</p>
        <img src={props.image}/>
        <button onClick={handleClick}>Добавить в корзину</button>
        </div>
    );
}    
export default ProductCard;