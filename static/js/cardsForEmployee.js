const card = document.getElementById('card');
var numCards = cards.length;

var j = 1;

const noCardToShowHTML = `
  <h3>No more cards to show :/</h3>
  <p>You've browsed through 'em all! Try refreshing to see if there's anything new</p>
`

const parseEmployerCard = (card) => {
  var value = `
    <h1>${card.name}</h1>
  `;
  if (card.company) {
    value += `<h3>${card.company.name}</h3>`
    value += `
      <h3>Bio: </h3>
      <p>${company.bio}</p>
    `
  }
};

if (cards.length === 0) {
  card.innerHTML = noCardToShowHTML;
} else {
  card.innerHTML = parseEmployeeCard(cards[0]);
}

document.getElementById('nextCard').onclick = () => {
  if (numCards === 0) {
    card.innerHTML = noCardToShowHTML;
  }
  j = (j++) % numCards;
  card.innerHTML = parseEmployeeCard(cards[0]);
};
