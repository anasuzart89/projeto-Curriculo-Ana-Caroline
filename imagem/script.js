
const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');

const gridSize = 20;
let snake = [{ x: 200, y: 200 }];
let direction = 'right';
let food = generateFood();
let score = 0;

document.addEventListener('keydown', (e) => {
    const key = e.key;
    if (key === 'ArrowUp' && direction !== 'down') direction = 'up';
    if (key === 'ArrowDown' && direction !== 'up') direction = 'down';
    if (key === 'ArrowLeft' && direction !== 'right') direction = 'left';
    if (key === 'ArrowRight' && direction !== 'left') direction = 'right';
});

function generateFood() {
    return {
        x: Math.floor(Math.random() * (canvas.width / gridSize)) * gridSize,
        y: Math.floor(Math.random() * (canvas.height / gridSize)) * gridSize,
    };
}

function gameLoop() {
    const head = { ...snake[0] };

    if (direction === 'up') head.y -= gridSize;
    if (direction === 'down') head.y += gridSize;
    if (direction === 'left') head.x -= gridSize;
    if (direction === 'right') head.x += gridSize;

    snake.unshift(head);

    if (head.x === food.x && head.y === food.y) {
        score++;
        document.getElementById('score').innerText = score;
        food = generateFood();
    } else {
        snake.pop();
    }

    if (head.x < 0 || head.y < 0 || head.x >= canvas.width || head.y >= canvas.height ||
        snake.slice(1).some(s => s.x === head.x && s.y === head.y)) {
        alert('Game Over! Pontuação: ' + score);
        snake = [{ x: 200, y: 200 }];
        direction = 'right';
        score = 0;
        document.getElementById('score').innerText = score;
        food = generateFood();
    }

    ctx.fillStyle = '#000';
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    ctx.fillStyle = '#0f0';
    ctx.fillRect(food.x, food.y, gridSize, gridSize);

    ctx.fillStyle = '#800080';
    snake.forEach(part => ctx.fillRect(part.x, part.y, gridSize, gridSize));
}

setInterval(gameLoop, 150);
