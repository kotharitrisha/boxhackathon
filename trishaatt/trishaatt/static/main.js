$(document).ready(function(){ 	
    console.log("I am up");
    
    projects_table = $('#projects-table').dataTable({
		"sDom": '<"top"f<"clear">>rt<"bottom"ilp<"clear">>',
        "bPaginate": false,
        "bInfo": false,
        "bAutoWidth": false,
        "bFilter": false,
        "sWidth": "100%",
        "aoColumns": [			
        	{"bSortable": false, "sWidth": "100%"}
        ]
    
    });
    
    
    tasks_table = $('#tasks-table').dataTable({
		"sDom": '<"top"f<"clear">>rt<"bottom"ilp<"clear">>',
        "bPaginate": false,
        "bInfo": false,
        "bAutoWidth": false,
        "bFilter": false,
        "sWidth": "100%",
        "aoColumns": [			
        	{"bSortable": false, "sWidth": "20%"},
        	{"bSortable": false, "sWidth": "60%"},
        	{"bSortable": false, "sWidth": "20%"}
        ]
    
    });
    
    get_projects = function(params) {
		/*
		var jaqxhr = $.post("/ajax/project_search/",
			{},
			function(data){
				populate_projects_table(data);
			}); 
			*/
			populate_projects_table(null);
	}
	
	
	get_tasks = function(params) {
		/*
		var jaqxhr = $.post("/ajax/project_search/",
			{},
			function(data){
				populate_projects_table(data);
			}); 
			*/
			populate_tasks_table(null);
	}
	
	
	function populate_projects_table(data){
		console.log("Inside Populate Projects");
		for(var i = 0; i< 15; i++){
			curr = projects_table.fnAddData( [
								'Trisha Kothari'
							  ]);	
							  
			curr_row = projects_table.fnGetNodes(curr);
			$(curr_row).click(get_tasks);
		}
		
	}
	
	
	function populate_tasks_table(data){
		console.log("Inside Populate Tasks");
		for(var i = 0; i< 15; i++){
		curr = tasks_table.fnAddData( [
       						'Trisha',
       						'Needs to sleep',
       						 'now.'
		                  ]);					
		}	
	}
	
	get_projects();
	 
});
