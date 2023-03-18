var dragAreaVideo = document.querySelector(".video")
var dragImg1 = document.querySelector(".img1")
var dragImg2 = document.querySelector(".img2")
var dragImg3 = document.querySelector(".img3")
var dragPdf1 = document.querySelector(".pdf1")
var pdf2 = document.querySelector(".pdf2")

$(document).ready(function () {

	var current_fs, next_fs, previous_fs; //fieldsets
	var opacity;
	var current = 1;
	var data = {
		"projectTitle": "",
		"category": "",
		"subCategory": "",
		"searchTag": [],
		"priceValue": {},
		"description": "",
		"FAQ": {},
		"requiredNote": "",
		"img1": "",
		"img2": "",
		"img3": "",
		"pdf1f": "",
		"pdf2": "",
		"video": "",
	}
	let serviceValue = []
	var pay_count = 0;
	var countFAQ = 0;

	var steps = $("fieldset").length;
	
	$(function(){
		$.ajax({
			method: "GET",
			url: "/listcategory",
			success: function (response) {
				// document.querySelector(".lang_level").innerHTML = ""
				var doc = document.querySelector(".category")
				response.map(data => {
					let value = `<option>${data.name}</option>`;
					$(".category").append(value)
				})
				// document.querySelector(".lang_level").innerHTML = result
			},
			error: function (e) {
				console.log(e)
				return false;
			}
		})
	})
	$(".addBtn-search").click(() => {
		var searchTag = $(".search-tag").val().trim();
		if (searchTag != "" && searchTag != " " && searchTag != "\n") {
			if (data["searchTag"].length <= 4){
			$(".add-search").append(`
			<div class="col-2 border bg-primary text-light text-align rounded-5">${searchTag}</div>
		`);
			data["searchTag"].push(searchTag);
			document.querySelector(".search-tag").value = "";
			}
			if (data["searchTag"].length > 4) {
			Swal.fire(
					'Error',
					"You have reached maximum limit",
					'warning'
			)
			document.querySelector(".search-tag").value = "";
				return false;
		}
			}
	})

	$(".serviceBtn").click(() => {
		var serviceInput = $(".serviceInput").val().trim();
		if (serviceInput != "" && serviceInput != " " && serviceInput != "\n") {
			if (serviceValue.length <= 7){
			$(".add-service").append(`
			<h3 class="fw-bolder lead border border-primary my-3 py-3 px-3 rounded-3 text-primary">${serviceInput}</h3>
		`);
			serviceValue.push(serviceInput);
			document.querySelector(".serviceInput").value = "";
			}
			if (serviceValue.length > 7) {
			Swal.fire(
					'Error',
					"You have reached maximum limit",
					'warning'
			)
			document.querySelector(".serviceInput").value = "";
				return false;
		}
			}
	})

	$(".addFAQ").click(() => {
		var question = $(".question").val().trim();
		var answer = $(".answer").val().trim();
		if (question == "" | question == " ") {
			Swal.fire(
					'Error',
					"question can't be empty",
					'warning'
			)
			return false;
			}
		if (answer == "" | answer == " ") {
			Swal.fire(
					'Error',
					"answer can't be empty",
					'warning'
			)
			return false;
		}
		var anon = {}
		anon["question"] = question;
		anon["answer"] = answer;
		data["FAQ"][countFAQ] = anon;
		countFAQ++;
		document.querySelector(".question").value = "";
		document.querySelector(".answer").value = "";
		$(".faq").append(`<div class="accordion-item">
                                            <h4 class="accordion-header" id="headingOne">
                                                <button class="accordion-button" type="button" data-bs-toggle="collapse"
                                                    data-bs-target="#collapse${countFAQ}" aria-expanded="true"
                                                    aria-controls="collapseOne">${question}
                                                </button>
                                            </h4>
                                            <div id="collapse${countFAQ}" class="accordion-collapse collapse"
                                                aria-labelledby="headingOne" data-bs-parent="#accordionExample">
                                                <div class="accordion-body text-lg-start">${answer}
                                                </div>
                                            </div>
                                        </div>`)
	})
	
	$(".addPayment").click(() => {
		var payment = {}

		var payType = $(".payType").val().trim()
		var payHead = $(".payHeading").val().trim()
		var colorValue = $(".colorValue").val().trim()
		var price = $(".price").val().trim()
		var duration = $(".duration").val().trim()
		if (payHead == "") {
			Swal.fire(
					'Error',
					"price heading can't be left empty",
					'warning'
			)
			return false;
		}

		if (price == "") {
			Swal.fire(
					'Error',
					"price can't be left empty",
					'warning'
			)
			return false;
		}
		if (serviceValue.length <= 0) {
				Swal.fire(
					'Error',
					"service can't be left empty",
					'warning'
				)
				return false;
		}
		if (pay_count > 2) {
			Swal.fire(
				'Error',
				"price packages can't be more than three",
				'warning'
			)
			return false;
		}
		payment["payType"] = payType
		payment["payHead"] = payHead
		payment["colorValue"] = colorValue
		payment["price"] = price
		payment["duration"] = duration
		payment["serviceValue"] = serviceValue

		$(".payItem").append(`<div class="accordion-item">
                                        <h2 class="accordion-header" id="flush-heading-${pay_count}">
                                            <button
                                                class="accordion-button p-3 border border-primary btn btn-outline-primary fs-5 fw-bolder text-muted"
                                                type="button" data-bs-toggle="collapse"
                                                data-bs-target="#flush-collapse-${pay_count}" aria-expanded="false"
                                                aria-controls="flush-collapse-${pay_count}">
                                                ${payType}
                                            </button>
                                        </h2>
                                        <div id="flush-collapse-${pay_count}" class="accordion-collapse collapse"
                                            aria-labelledby="flush-heading-2" data-bs-parents="#questions">
                                            <div class="accordion-body border">
                                                <div class="col d-flex justify-content-center">
                                                    <div class="card mb-4 rounded-3 shadow-sm w-50 mt-4">
                                                        <div class="card-header py-3 bg-${colorValue} text-light">
                                                            <h4 class="my-0 fw-normal">${payHead}</h4>
                                                        </div>
                                                        <div class="card-body">
                                                            <h1 class="card-title pricing-card-title">${price}<small
                                                                    class="text-muted fw-light"> Ethers</small></h1>
                                                            <ul class="list-unstyled mt-3 mb-4">	
                                                                (services appear here)
                                                            </ul>
                                                            <button type="button"
                                                                class="w-100 btn btn-lg btn-outline-primary">Continue
                                                                with ${price} Ethers (${duration})</button>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>`)
		data["priceValue"][pay_count] = payment
		serviceValue = []
		document.querySelector(".payHeading").value = ""
		document.querySelector(".price").value = ""
		document.querySelector(".add-service").textContent = "";
		pay_count+=1
		console.log("count", pay_count)

	})

$(".video").click(() => {
	document.querySelector(".videoInput").click()
})
$(".img1").click(() => {
	document.querySelector(".img1Input").click()
})
$(".img2").click(() => {
	if (data["img1"] != ""){
		document.querySelector(".img2Input").click()
	}
	else {
		Swal.fire(
					'Error',
					"Click on the first Image Field",
					'warning'
		)
			return false;
	}
})
$(".img3").click(() => {
	if (data["img1"] != "" & data["img2"] != ""){
		document.querySelector(".img3Input").click()
	}
	else if (data["img1"] == "") {
		Swal.fire(
					'Error',
					"Click on the first Image Field",
					'warning'
		)
			return false;
	}
	else {
		Swal.fire(
					'Error',
					"Click on the second Image Field",
					'warning'
		)
			return false;
	}
})
$(".pdf1").click(() => {
	document.querySelector(".pdf1Input").click()
})
	
	$(".pdf2").click(() => {
	if (data["pdf1f"] != ""){
		document.querySelector(".pdf2Input").click()
	}
	else {
		Swal.fire(
					'Error',
					"Click on the first PDF Field",
					'warning'
		)
			return false;
	}
})
	
	dragAreaVideo.addEventListener("dragover", (e) => {
  e.preventDefault();
  dragAreaVideo.classList.add("dragError")
  dragAreaVideo.classList.remove("dragSuccess")
	dragAreaVideo.classList.remove("dragHover")
	Swal.fire(
					'Error',
					"we don't support drag and drop for now",
					'warning'
			)
			return false;
})
dragAreaVideo.addEventListener("dragleave", (e) => {
  dragAreaVideo.classList.remove("dragError")
  dragAreaVideo.classList.remove("dragHover")
  dragAreaVideo.classList.remove("dragSuccess")
})
document.querySelector(".videoInput").addEventListener("change", (e) =>{
	e.preventDefault();
  dragAreaVideo.classList.remove("dragError")
  dragAreaVideo.classList.remove("dragHover")
	dragAreaVideo.classList.add("dragSuccess")
	let folder = e.target.files[0];
  if (folder.type == "video/mp4") {
    console.log(folder)
  let fileReader = new FileReader();
  fileReader.onload = ()=>{
    let fileURL = fileReader.result;
    document.querySelector(".videoNum").textContent = "(1/1)";
		dragAreaVideo.style.background.url = fileURL;
		data["video"] = folder.name
  };
  fileReader.readAsDataURL(folder);
  }
  else {
		document.querySelector(".videoNum").textContent = "(0/1)";
    dragAreaVideo.classList.add("dragError")
    dragAreaVideo.classList.remove("dragHover")
		dragAreaVideo.classList.remove("dragSuccess")
		Swal.fire(
					'Error',
					"Unsupported Format (mp4 format only)",
					'warning'
			)
			return false;
  }
})
	
dragImg1.addEventListener("dragover", (e) => {
	e.preventDefault();
	dragImg1.classList.add("dragError")
  dragImg1.classList.remove("dragSuccess")
	dragImg1.classList.remove("dragHover")
	Swal.fire(
					'Error',
					"we don't support drag and drop for now",
					'warning'
			)
			return false;
})
dragImg1.addEventListener("dragleave", (e) => {
  dragImg1.classList.remove("dragError")
  dragImg1.classList.remove("dragHover")
  dragImg1.classList.remove("dragSuccess")
})
document.querySelector(".img1Input").addEventListener("change", (e) =>{
  e.preventDefault();
  dragImg1.classList.remove("dragError")
  dragImg1.classList.remove("dragHover")
	dragImg1.classList.add("dragSuccess")
	let folder = e.target.files[0];
  if (folder.type == "image/png" | folder.type == "image/jpeg") {
    console.log(folder)
  let fileReader = new FileReader();
  fileReader.onload = ()=>{
    let fileURL = fileReader.result;
    document.querySelector(".imgNum").textContent = "(1/3)";
		dragImg1.style.background.url = fileURL;
		data["img1"] = folder.name
  };
  fileReader.readAsDataURL(folder);
  }
  else {
		document.querySelector(".imgNum").textContent = "(1/3)";
    dragImg1.classList.add("dragError")
    dragImg1.classList.remove("dragHover")
		dragImg1.classList.remove("dragSuccess")
		Swal.fire(
					'Error',
					"Unsupported Format (png/jpeg format only)",
					'warning'
			)
			return false;
  }
})
	
dragImg2.addEventListener("dragover", (e) => {
  e.preventDefault();
  dragImg2.classList.add("dragError")
  dragImg2.classList.remove("dragSuccess")
	dragImg2.classList.remove("dragHover")
	Swal.fire(
					'Error',
					"we don't support drag and drop for now",
					'warning'
			)
			return false;
})
dragImg2.addEventListener("dragleave", (e) => {
  dragImg2.classList.remove("dragError")
  dragImg2.classList.remove("dragHover")
  dragImg2.classList.remove("dragSuccess")
})
document.querySelector(".img2Input").addEventListener("change", (e) =>{
  e.preventDefault();
  dragImg2.classList.remove("dragError")
  dragImg2.classList.remove("dragHover")
	dragImg2.classList.add("dragSuccess")
	let folder = e.target.files[0];
	if (folder.type == "image/png" | folder.type == "image/jpeg") {
  let fileReader = new FileReader();
  fileReader.onload = ()=>{
    let fileURL = fileReader.result;
    document.querySelector(".imgNum").textContent = "(2/3)";
		dragImg2.style.background.url = fileURL;
		data["img2"] = folder.name
  };
  fileReader.readAsDataURL(folder);
  }
  else {
		document.querySelector(".imgNum").textContent = "(1/3)";
    dragImg2.classList.add("dragError")
    dragImg2.classList.remove("dragHover")
		dragImg2.classList.remove("dragSuccess")
		Swal.fire(
					'Error',
					"Unsupported Format (png/jpeg format only)",
					'warning'
			)
			return false;
  }
})
dragImg3.addEventListener("dragover", (e) => {
  e.preventDefault();
  dragImg3.classList.add("dragError")
  dragImg3.classList.remove("dragSuccess")
	dragImg3.classList.remove("dragHover")
	Swal.fire(
					'Error',
					"we don't support drag and drop for now",
					'warning'
			)
			return false;
})
dragImg3.addEventListener("dragleave", (e) => {
  dragImg3.classList.remove("dragError")
  dragImg3.classList.remove("dragHover")
  dragImg3.classList.remove("dragSuccess")
})
document.querySelector(".img3Input").addEventListener("change", (e) =>{
  e.preventDefault();
  dragImg3.classList.remove("dragError")
  dragImg3.classList.remove("dragHover")
	dragImg3.classList.add("dragSuccess")
	let folder = e.target.files[0];
  if (folder.type == "image/png" | folder.type == "image/jpeg") {
    console.log(folder)
  let fileReader = new FileReader();
  fileReader.onload = ()=>{
    let fileURL = fileReader.result;
    document.querySelector(".imgNum").textContent = "(3/3)";
		dragImg3.style.background.url = fileURL;
		data["img3"] = folder.name
  };
  fileReader.readAsDataURL(folder);
  }
  else {
		document.querySelector(".imgNum").textContent = "(2/3)";
    dragImg3.classList.add("dragError")
    dragImg3.classList.remove("dragHover")
		dragImg3.classList.remove("dragSuccess")
		Swal.fire(
					'Error',
					"Unsupported Format (png/jpeg format only)",
					'warning'
			)
			return false;
  }
})

dragPdf1.addEventListener("dragover", (e) => {
  e.preventDefault();
  dragPdf1.classList.add("dragError")
  dragPdf1.classList.remove("dragSuccess")
	dragPdf1.classList.remove("dragHover")
	Swal.fire(
					'Error',
					"we don't support drag and drop for now",
					'warning'
			)
			return false;
})
dragPdf1.addEventListener("dragleave", (e) => {
  dragPdf1.classList.remove("dragError")
  dragPdf1.classList.remove("dragHover")
  dragPdf1.classList.remove("dragSuccess")
})
document.querySelector(".pdf1Input").addEventListener("change", (e) =>{
  e.preventDefault();
  dragPdf1.classList.remove("dragError")
  dragPdf1.classList.remove("dragHover")
  dragPdf1.classList.add("dragSuccess")
	let folder = e.target.files[0];
  if (folder.type == "application/pdf") {
    console.log(folder)
  let fileReader = new FileReader();
  fileReader.onload = ()=>{
    let fileURL = fileReader.result;
    document.querySelector(".pdfNum").textContent = "(1/2)";
		dragPdf1.style.background.url = fileURL;
		data["pdf1f"] = folder.name
  };
  fileReader.readAsDataURL(folder);
  }
	else {
		console.log(folder.type)
		document.querySelector(".pdfNum").textContent = "(0/2)";
    dragPdf1.classList.add("dragError")
  	dragPdf1.classList.remove("dragHover")
		dragPdf1.classList.remove("dragSuccess")
		Swal.fire(
					'Error',
					"Unsupported Format (pdf format only)",
					'warning'
			)
			return false;
  }
})
pdf2.addEventListener("dragover", (e) => {
  e.preventDefault();
  pdf2.classList.add("dragError")
  pdf2.classList.remove("dragSuccess")
	pdf2.classList.remove("dragHover")
	Swal.fire(
					'Error',
					"we don't support drag and drop for now",
					'warning'
			)
			return false;
})
pdf2.addEventListener("dragleave", (e) => {
  pdf2.classList.remove("dragError")
  pdf2.classList.remove("dragHover")
  pdf2.classList.remove("dragSuccess")
})
document.querySelector(".pdf2Input").addEventListener("change", (e) =>{
  e.preventDefault();
  pdf2.classList.remove("dragError")
  pdf2.classList.remove("dragHover")
  pdf2.classList.add("dragSuccess")
	let folder = e.target.files[0];
  if (folder.type == "application/pdf") {
    console.log(folder)
  let fileReader = new FileReader();
  fileReader.onload = ()=>{
    let fileURL = fileReader.result;
    document.querySelector(".pdfNum").textContent = "(2/2)";
		pdf2.style.background.url = fileURL;
		data["pdf2"] = folder.name
  };
  fileReader.readAsDataURL(folder);
  }
	else {
		console.log(folder.type)
		document.querySelector(".pdfNum").textContent = "(1/2)";
    pdf2.classList.add("dragError")
  	pdf2.classList.remove("dragHover")
		pdf2.classList.remove("dragSuccess")
		Swal.fire(
					'Error',
					"Unsupported Format (pdf format only)",
					'warning'
			)
			return false;
  }
})
	$(".category").on("change", (e) => {
		var cat = $(".category").val().trim();
		if (cat) {
			$.ajax({
			method: "GET",
			url: "/listsubcategory",
			data: {"category": cat},
			success: function (response) {
				document.querySelector(".sub-category").innerHTML = `<option value="">SELECT A SUBCATEGORY</option>`
				var doc = document.querySelector(".sub-category")
				response.map(datar => {
					let value = `<option>${datar.name}</option>`;
					$(".sub-category").append(value)
				})
				// document.querySelector(".lang_level").innerHTML = result
			},
			error: function (e) {
				console.log(e)
				return false;
			}
		})
		}
	})	
	$(".next").click(async function () {

		current_fs = $(this).parent();
		next_fs = $(this).parent().next();

		if (current == 1) {
			var projectTitle = $(".meta-title").val().trim();
			var category = $(".category").val().trim();
			var subCategory = $(".sub-category").val().trim();
			if (projectTitle == "" | projectTitle == " ") {
				Swal.fire(
					'Error',
					"meta title can't be empty",
					'warning'
				)
				return false;
			}
			if (category == "" | category == " ") {
				Swal.fire(
					'Error',
					"category can't be left empty",
					'warning'
				)
				return false;
			}
			if (subCategory == "" | subCategory == " ") {
				Swal.fire(
					'Error',
					"subCategory can't be left empty",
					'warning'
				)
				return false;
			}
			if (data["searchTag"].length <= 0) {
				Swal.fire(
					'Error',
					"Search keyword can't be left empty",
					'warning'
				)
				return false;
			}
			const { value: confirmText } = await Swal.fire({
				title: 'Are you sure?',
				text: "You won't be able to go back!",
				input: 'text',
				inputLabel: 'type nodepair',
				showCancelButton: true,
				allowOutsideClick: false,
				inputValidator: (value) => {
				  if (!value | value != "nodepair") {
					return 'You need to write nodepair in the input field!'
				  }
				}
			  })
			  
			  if (confirmText == "nodepair") {
				Swal.fire(
					'Ok!',
					'Saved Sucessfully.',
					'success'
				  )
			  }
			 else{
				return false;
			 }
			data["projectTitle"] = projectTitle
			data["category"] = category
			data["subCategory"] = subCategory
			console.log(data)
		}

		if (current == 2) {
			console.log(pay_count)
			if (pay_count < 3) {
				Swal.fire(
					'Error',
					"Payment packages must be three",
					'warning'
				)
				return false;
			}
			const { value: confirmText } = await Swal.fire({
				title: 'Are you sure?',
				text: "You won't be able to go back!",
				input: 'text',
				inputLabel: 'type nodepair',
				showCancelButton: true,
				allowOutsideClick: false,
				inputValidator: (value) => {
				  if (!value | value != "nodepair") {
					return 'You need to write nodepair in the input field!'
				  }
				}
			  })
			  
			  if (confirmText == "nodepair") {
				Swal.fire(
					'Ok!',
					'Saved Sucessfully.',
					'success'
				  )
			  }
			 else{
				return false;
			 }
			console.log(data)
		}

		if (current == 3) {
			var description = $(".description").val().trim();
			if (description == "" | description == " ") {
				Swal.fire(
					'Error',
					"description can' be left empty.",
					'warning'
				)
				return false;
			}
			const { value: confirmText } = await Swal.fire({
				title: 'Are you sure?',
				text: "You won't be able to go back!",
				input: 'text',
				inputLabel: 'type nodepair',
				showCancelButton: true,
				allowOutsideClick: false,
				inputValidator: (value) => {
				  if (!value | value != "nodepair") {
					return 'You need to write nodepair in the input field!'
				  }
				}
			  })
			  
			  if (confirmText == "nodepair") {
				Swal.fire(
					'Ok!',
					'Saved Sucessfully.',
					'success'
				  )
			  }
			 else{
				return false;
			 }
			data["description"] = description;
			console.log(data)
		}

		if (current == 4) {
			var note = $(".requireNote").val().trim()
			if (note != "") {
				const { value: confirmText } = await Swal.fire({
					title: 'Are you sure?',
					text: "You won't be able to go back!",
					input: 'text',
					inputLabel: 'type nodepair',
					showCancelButton: true,
					allowOutsideClick: false,
					inputValidator: (value) => {
					  if (!value | value != "nodepair") {
						return 'You need to write nodepair in the input field!'
					  }
					}
				  })
				  
				  if (confirmText == "nodepair") {
					Swal.fire(
						'Ok!',
						'Saved Sucessfully.',
						'success'
					  )
				  }
				 else{
					return false;
				 }
				data["requiredNote"] = note
			}
			
		}
		if (current == 5) {
			if ((data["img1"] == data["img2"]) & data["img1"] != "") {
				Swal.fire(
					'Error',
					"you can't upload similar images",
					'warning'
				)
				return false;
			}
			if ((data["img1"] == data["img3"]) & data["img1"] != "") {
				Swal.fire(
					'Error',
					"you can't upload similar images",
					'warning'
				)
				return false;
			}
			if ((data["img2"] == data["img3"]) & data["img2"] != "") {
				Swal.fire(
					'Error',
					"you can't upload similar images",
					'warning'
				)
				return false;
			}
			if (data["img2"] == "") {
				Swal.fire(
					'Error',
					"you must upload at least two different images",
					'warning'
				)
				return false;
			}
			const { value: confirmText } = await Swal.fire({
				title: 'Are you sure?',
				text: "You won't be able to go back!",
				input: 'text',
				inputLabel: 'type nodepair',
				showCancelButton: true,
				allowOutsideClick: false,
				inputValidator: (value) => {
				  if (!value | value != "nodepair") {
					return 'You need to write nodepair in the input field!'
				  }
				}
			  })
			  
			  if (confirmText == "nodepair") {
				Swal.fire(
					'Ok!',
					'Saved Sucessfully.',
					'success'
				  )
			  }
			 else{
				return false;
			 }
			console.log(data)
			document.querySelector(".data").value = JSON.stringify(data);
		}
		//Add Class Active
		$("#progressbar li").eq($("fieldset").index(next_fs)).addClass("active");

		//show the next fieldset
		next_fs.show();
		//hide the current fieldset with style
		current_fs.animate({ opacity: 0 }, {
			step: function (now) {
				// for making fielset appear animation
				opacity = 1 - now;

				current_fs.css({
					'display': 'none',
					'position': 'relative'
				});
				next_fs.css({ 'opacity': opacity });
			},
			duration: 500
		});
		setProgressBar(++current);
	});

	function setProgressBar(curStep) {
		var percent = parseFloat(100 / steps) * curStep;
		percent = percent.toFixed();
		$(".progress-bar")
			.css("width", percent + "%")
	}

	$(".submit").click(function () {
		return false;
	})
	
});
