/* Simple browser-based Tic Tac Toe game */

const boardElem = document.getElementById('tic-tac-toe-board');
const messageElem = document.getElementById('tic-message');

let board = Array(9).fill(null);
let currentPlayer = 'X';
let gameOver = false;

const winCombos = [
  [0,1,2], [3,4,5], [6,7,8],
  [0,3,6], [1,4,7], [2,5,8],
  [0,4,8], [2,4,6]
];

function initBoard() {
  boardElem.innerHTML = '';
  board.forEach((cell, idx) => {
    const cellElem = document.createElement('div');
    cellElem.className = 'tic-cell';
    cellElem.dataset.index = idx;
    cellElem.addEventListener('click', onCellClick);
    cellElem.textContent = cell || '';
    boardElem.appendChild(cellElem);
  });
}

function onCellClick(e) {
  const idx = Number(e.currentTarget.dataset.index);
  if (gameOver || board[idx]) return;
  board[idx] = currentPlayer;
  e.currentTarget.textContent = currentPlayer;

  if (checkWinner(currentPlayer)) {
    showMessage(`Player ${currentPlayer} wins!`);
    gameOver = true;
    disableBoard();
    return;
  }

  if (board.every(cell => cell)) {
    showMessage("It's a tie!");
    gameOver = true;
    return;
  }

  currentPlayer = currentPlayer === 'X' ? 'O' : 'X';
  showMessage(`Player ${currentPlayer}'s turn`);
}

function checkWinner(player) {
  return winCombos.some(combo =>
    combo.every(i => board[i] === player)
  );
}

function showMessage(msg) {
  messageElem.textContent = msg;
  messageElem.classList.remove('hidden');
}

function disableBoard() {
  document.querySelectorAll('.tic-cell').forEach(cell => {
    cell.classList.add('disabled');
  });
}

function resetGame() {
  board = Array(9).fill(null);
  currentPlayer = 'X';
  gameOver = false;
  messageElem.classList.add('hidden');
  initBoard();
}

// initialize on load
initBoard();
showMessage(`Player ${currentPlayer}'s turn`);

// optional: expose reset for console or future button
window.ticTacToeReset = resetGame;
