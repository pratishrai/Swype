const card = document.getElementById('card');
var numCards = cards.length;

var j = 1;

const noCardToShowHTML = `
  <h3>No more cards to show :/</h3>
  <p>You've browsed through 'em all! Try refreshing to see if there's anything new</p>
`

const parseEmployerCard = (givenCard) => {
  var value = `
    <h1>${givenCard.name}</h1>
  `;
  if (givenCard.company) {
    value += `<h3>Company: ${givenCard.company.name}</h3>`
    value += `
      <h3>Bio: </h3>
      <p>${givenCard.company.bio}</p>
    `
  }
  if (givenCard.tags) {
    value += `<h3>Looking for:</h3>\n<ul>\n`;
    for (var i = 0; i < givenCard.tags.length; i++) {
      value += `<li>${givenCard.tags[i]}</li>\n`;
    }
    value += `</ul>`;
  }
  return value;
};

if (cards.length === 0) {
  card.innerHTML = noCardToShowHTML;
} else {
  card.innerHTML = parseEmployerCard(cards[0]);
}

document.getElementById('nextCard').onclick = () => {
  if (numCards === 0) {
    card.innerHTML = noCardToShowHTML;
  }
  j = (j++) % numCards;
  card.innerHTML = parseEmployerCard(cards[0]);
};
