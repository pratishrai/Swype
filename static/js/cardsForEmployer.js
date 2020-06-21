const card = document.getElementById('card');
var numCards = cards.length;
var currentCardId = null;

var j = 1;

const noCardToShowHTML = `
  <h3>No more cards to show :/</h3>
  <p>You've browsed through 'em all! Try refreshing to see if there's anything new</p>
`

const parseEmployeeCard = (givenCard) => {
  var value = `
    <h1>${givenCard.name}</h1>
  `;
  if (givenCard.tags) {
    value += `
      <h3>Skills:</h3>
      <ul>
    `;
    for (i = 0; i < givenCard.tags.length; i++) {
      value += `<li>${givenCard.tags[i]}</li>\n`;
    }
    value += "</ul>";
  }
  value += "<h3>Bio:</h3>";
  value += `<p>${givenCard.bio}</p>`
  value += `<button class="btn btn-secondary" type="button" name="button" onclick="nextHandler()">Next</button>`
  value += `<button class="btn btn-success" type="button" name="button" onclick="interestedHandler()">Interested 👍</button>`
  currentCardId = givenCard.id;
  return value;
};

if (cards.length === 0) {
  card.innerHTML = noCardToShowHTML;
} else {
  card.innerHTML = `
    <div class="jumbotron jumbotron-fluid bg-primary text-light">
        ${parseEmployeeCard(cards[0])}
    </div>
  `
}

const nextHandler = () => {
  if (numCards === 0) {
    card.innerHTML = noCardToShowHTML;
  }
  j++;
  j %= numCards;
  card.innerHTML = `
    <div class="jumbotron jumbotron-fluid bg-primary text-light">
      ${parseEmployeeCard(cards[j])}
    </div>
  `;
};

const interestedHandler = () => {
  cards.splice(j, 1);
  numCards--;
  j--;
  fetch(window.location.href + `/markInterest?employee_id=${currentCardId}`)
    .then((response) => {
      return response.json();
    })
    .catch((error) => {
      return error;
    });
  nextHandler();
};
