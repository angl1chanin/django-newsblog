const manageBtn = document.querySelector('.manage__sort-btn');
const arrowManageBtn = manageBtn.getElementsByTagName('svg');
const manageDropdown = document.querySelector('.manage__sort-dropdown');

manageBtn.addEventListener('click', () => {
  manageDropdown.classList.toggle('active');
  arrowManageBtn[0].classList.toggle('active');
});
