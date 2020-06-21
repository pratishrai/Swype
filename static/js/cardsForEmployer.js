const card = document.getElementById('card');
var numCards = cards.length;

var j = 1;

const noCardToShowHTML = `
  <h3>No more cards to show :/</h3>
  <p>You've browsed through 'em all! Try refreshing to see if there's anything new</p>
`

const parseEmployeeCard = (givenCard) => {
  var value = `
    <h1>${givenCard.name}</h1>
  `;
  if (givenCard.skills) {
    value += `
      <h3>Skills:</h3>
      <ul>
    `;
    for (i = 0; i < givenCard.skills.length; i++) {
      value += `<li>${givenCard.skills[i]}</li>\n`;
    }
    value += "</ul>";
  }
  value += "<h3>Bio:</h3>";
  value += `<p>${givenCard.bio}</p>`
  return value;
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
