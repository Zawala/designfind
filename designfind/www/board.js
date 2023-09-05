frappe.ready(function() {
	const loginButton = $('.btn-login-area');
    const box = document.getElementsByClassName('card');

    const allChildren = box.length;
    console.log(allChildren);
    frappe.call({
        method: "designfind.www.board.init_load",
        args: {
                    number:allChildren
        },
        callback: function(r){
        posts = r.message;
        const row = document.querySelector('.capsule'); 

        posts.forEach(post => {

            const col = document.createElement('div');
            col.className = 'col';
          
            // Add card content
            col.innerHTML = `
            <div class="col">
          <div class="card shadow-sm">
              <img src='${post[3]}' alt="Thumbnail" class="bd-placeholder-img card-img-top" width="100%" height="225">
              <div class="card-body">
                  <p class="card-text">'${post[1]}'</p>
                  <div class="d-flex justify-content-between align-items-center">
                      <div class="btn-group">
                        <a href='${post[4]}' target="_blank"><button type="button" class="btn btn-sm btn-outline-secondary">View</button></a>
                          <button type="button" class="btn btn-sm btn-outline-secondary">Contact</button>
                      </div>
                      <span><small class="text-body-secondary">${post[0]}</small></span>
                  </div>
              </div>
          </div>
      </div>
            `;
          
            row.appendChild(col);
          
          });
    }
        });
})


$( "#load" ).click(function (event) {
    event.preventDefault();
    const box = document.getElementsByClassName('card');

    const allChildren = box.length;
    console.log(allChildren);
    frappe.call({
        method: "designfind.www.board.get_posts",
        args: {
                    number:allChildren
        },
        callback: function(r){
        posts = r.message;
        const row = document.querySelector('.capsule'); 

        posts.forEach(post => {
            const col = document.createElement('div');
            col.className = 'col';
          
            // Add card content
            col.innerHTML = `
            <div class="col">
          <div class="card shadow-sm">
              <img src='${post[3]}' alt="Thumbnail" class="bd-placeholder-img card-img-top" width="100%" height="225">
              <div class="card-body">
                  <p class="card-text">'${post[1]}'</p>
                  <div class="d-flex justify-content-between align-items-center">
                      <div class="btn-group">
                        <a href='${post[4]}' target="_blank"><button type="button" class="btn btn-sm btn-outline-secondary">View</button></a>
                          <a href='${post[4]}' target="_blank"><button type="button" class="btn btn-sm btn-outline-secondary">Contact</button></a>
                      </div>
                      <small class="text-body-secondary">${post[2]}</small>
                  </div>
              </div>
          </div>
      </div>
            `;
          
            row.appendChild(col);
          
          });
    }
        });

});