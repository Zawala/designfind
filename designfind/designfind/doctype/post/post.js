// Copyright (c) 2023, Zawala and contributors
// For license information, please see license.txt

frappe.ui.form.on('Post', {
	delete: function(frm) {
		let text = element.textContent; 
		console.log('text');
	 }
	
});
$( "#delete" ).click(function (event) {
		event.preventDefault();
		let text = element.textContent; 
		console.log('text');



	});