document.addEventListener('DOMContentLoaded', function() {
  const navLinks = document.querySelectorAll('nav ul li a');
  navLinks.forEach(link => {
	link.addEventListener('click', function(event) {
	  event.preventDefault();
	  const targetId = this.getAttribute('href').substring(1);
	  const targetSection = document.getElementById(targetId);
	  if (targetSection) {
		window.scrollTo({
		  top: targetSection.offsetTop,
		  behavior: 'smooth'
		});
		// Aktiven Link setzen
		navLinks.forEach(link => link.classList.remove('active'));
		this.classList.add('active');
	  }
	});
  });

  // Formularvalidierung
  const form = document.getElementById('contactForm');
  const formError = document.getElementById('formError');
  form.addEventListener('submit', function(event) {
	formError.textContent = '';
	if (!form.checkValidity()) {
	  event.preventDefault();
	  formError.textContent = 'Bitte füllen Sie alle Felder korrekt aus.';
	}
  });

  // private _stream: Stream;
});