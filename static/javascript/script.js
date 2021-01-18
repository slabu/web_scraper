
var elem = document.querySelector('.posts_table');            


resultsTable(elem, 4, 4);

function resultsTable(parent, cols, rows) {
    var table = document.createElement('table');

    var header_tr = document.createElement('tr');

    var post_id_th = document.createElement('th');
    var post_id_th_text = document.createTextNode('post_id');
    post_id_th.appendChild(post_id_th_text);
    header_tr.appendChild(post_id_th);
                
                

    for (var title in posts['post_1']){

        var post_title = document.createElement('th');
        var post_title_text = document.createTextNode(title);
        post_title.appendChild(post_title_text);
        header_tr.append(post_title);

        console.log(title)
                    
    }
    table.appendChild(header_tr);
                


    for (var key in posts){
        var tr = document.createElement('tr');
        var post_id_td = document.createElement('td');
        var post_id_text = document.createTextNode(key);
        post_id_td.appendChild(post_id_text);
        tr.appendChild(post_id_td);

        for (var post in posts[key]){

            var td = document.createElement('td');
            var cell_text = document.createTextNode(posts[key][post]);
            td.appendChild(cell_text);
            tr.appendChild(td);


                        
        }
        table.appendChild(tr);
    }
    parent.appendChild(table);

}