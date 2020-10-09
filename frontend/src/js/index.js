import '../css/style.css';
import printStuff from './animate';
function component() {
    const element = document.createElement('div');
    element.innerHTML = (['Hello', 'webpack'], 'asdfjaskjlfa sdnfsadfj oas');
    element.classList.add('hello');

    const btn = document.createElement('button');
    btn.innerHTML = 'Click me and check the console!';
    btn.onclick = printStuff;
 
    element.appendChild(btn);
    return element;
}

document.body.appendChild(component())
