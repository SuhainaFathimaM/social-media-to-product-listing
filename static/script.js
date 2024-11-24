document.getElementById("upload-form").addEventListener("submit", async function(event) {
    event.preventDefault(); // Prevent default form submission

    // Select input elements
    let fileInput = document.getElementById("file-upload");
    let textInput = document.getElementById("text-input");

    // Validate inputs
    if (fileInput.files.length === 0 && !textInput.value.trim()) {
        alert("Please upload a file or enter some text.");
        return;
    }

    // Prepare FormData object
    let formData = new FormData();
    if (fileInput.files.length > 0) {
        formData.append("file", fileInput.files[0]);
    }
    if (textInput.value.trim()) {
        formData.append("text", textInput.value.trim());
    }

    // Show loading indicator (you need to create a loader element in HTML)
    const loader = document.getElementById("loading");
    if (loader) {
        loader.style.display = "block";
    }

    try {
        // Make the POST request
        let response = await fetch("/upload/", {
            method: "POST",
            body: formData
        });

        // Hide loader
        if (loader) {
            loader.style.display = "none";
        }

        if (response.ok) {
            let data = await response.json();

            // Update product listing
            if (data.product_listing) {
                document.getElementById("listing").textContent = data.product_listing ;
            }


            // Update processed file display
            if (data.processed_file_url) {
                let videoElement = document.getElementById("processed-video");
                let imageElement = document.getElementById("processed-image");

                if (data.processed_file_url.endsWith(".mp4")) {
                    videoElement.style.display = "block";
                    imageElement.style.display = "none";
                    videoElement.src = data.processed_file_url;
                } else {
                    imageElement.style.display = "block";
                    videoElement.style.display = "none";
                    imageElement.src = data.processed_file_url;
                }
            }
        } else {
            let errorMessage = `Error ${response.status}: ${response.statusText}`;
            console.error(errorMessage);
            alert("Failed to process your request. " + errorMessage);
        }
    } catch (error) {
        // Handle any network or unexpected errors
        console.error("Error occurred:", error);
        alert("An error occurred while uploading. Please try again.");
    } finally {
        // Hide loader even if an error occurs
        if (loader) {
            loader.style.display = "none";
        }
    }
});
