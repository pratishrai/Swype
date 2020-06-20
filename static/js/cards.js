const card = document.getElementById('card');
var cards = JSON.parse({{ cards }});
var numCards = cards.length;

var j = 1;

const noCardToShowHTML = `
  <h1>No more cards to show :/</h1>
  <p>You've browsed through 'em all! Try refreshing to see if there's anything new</p>
`

const parseCard = (card) => {
  var value = `
    <h1>${card.name}</h1>
  `;
  if (card.skills) {
    value += `
      <h3>Skills:</h3>
      <ul>
    `;
    for (i = 0; i < card.skills.length; i++) {
      value += `<li>${card.skills[i]}</li>\n`;
    }
    value += "</ul>";
  }
  value += "<h3>Bio</h3>";
  value += `<p>${card.bio}</p>`
};

if (cards.length === 0) {
  card.innerHTML = noCardToShowHTML;
} else {
  card.innerHTML = parseCard(cards[0]);
}

document.getElementById('nextCard').onclick = () => {
  if (numCards === 0) {
    card.innerHTML = noCardToShowHTML;
  }
  j = (j++) % numCards;
  card.innerHTML = parseCard(cards[0]);
};
