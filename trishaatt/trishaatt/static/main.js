

$(document).ready(function(){ 	
    console.log("I am up");  
    
	addTask = function(){
		$("#new-project-dialog").dialog("close");
		console.log("Add Task");
		var width = $(window).width();
		var height = $(window).height();

		// Provide some space between the window edges.
		var width = width - 100;
		var height = height - 100;
		var title = 'Add Task';	
		$("#new-task-dialog").dialog({ title: title, height: height, width: width, autoOpen:false, modal: true});		
		$("#new-task-dialog").dialog("open");
	}




	addMoreTask = function(){	
		console.log("Add More Task"); 
		$("#new-task-dialog").dialog("open");
	}

	doneAllTasks = function(){
		$("#new-task-dialog").dialog("close");
	} 
    
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
	
	
	add_project = function() {
		console.log("here");
		params = {};
		params.title = $("#project_title").val();
		params.desc = $("#project_desc").val();
		params.filename = $("#project_filename").val();
		console.log("params " +  params.toString());		
		var jaqxhr = $.post("/ajax/project_add/",
			{'title': params.title,
			'desc': params.desc,
			'filename': params.filename},
			function(data){
				addTask();
			}); 
			
			
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
