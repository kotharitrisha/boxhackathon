function addTask(){
	$("#new-project-dialog").dialog("destroy");
	var width = $(window).width();
	var height = $(window).height();

	// Provide some space between the window edges.
	var width = width - 100;
	var height = height - 100;
	var title = 'Add Task';
	$("#new-task-dialog").dialog({ title: title, height: height, width: width});
}

function showNext(){
	$("#new-task-dialog").dialog("destroy");
	var width = $(window).width();
	var height = $(window).height();

	// Provide some space between the window edges.
	var width = width - 100;
	var height = height - 100;
	var title = 'Add Task';
	$("#more-task-dialog").dialog({ title: title, height: height, width: width});
}

	

function addMoreTask(){	
	console.log("Add More Task"); 
	$("#more-task-dialog").dialog("destroy")
	var width = $(window).width();
	var height = $(window).height();

	// Provide some space between the window edges.
	var width = width - 100;
	var height = height - 100;
	var title = 'Add Task';
	$("#new-task-dialog-temp").dialog({ title: title, height: height, width: width});

}

function doneAllTasks(){
	console.log("Done Adding"); 
	$("#new-task-dialog").dialog('destroy');
}

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
			projects_table.fnClearTable();
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
			tasks_table.fnClearTable();
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
	
	new_project = function() {
		var width = $(window).width();
		var height = $(window).height();

		// Provide some space between the window edges.
		var width = width - 100;
		var height = height - 100;
		var title = 'New Project';
		$('#new-project-dialog').dialog({ title: title, height: height, width: width });
			
	}

	$('#new-project-link').click(new_project);
	get_projects();
	
});
