var csrf_token = document.getElementById('css_holder').value;

function translateText(){
    var text = document.getElementById('source-text').value;
    var src_lang = document.getElementById('source-language').value;
    var dest_lang = document.getElementById('target-language').value;

    if (text && src_lang != 'Detect Language' && dest_lang != 'Target Language'){

        $.ajax({
            url: "/api/translate/",
            type: "POST",
            data: {
                text: text,
                src_lang: src_lang,
                dest_lang: dest_lang,
                csrfmiddlewaretoken: csrf_token,
            },
            success: function(data) {
                // console.log(data);
                document.getElementById('translated-text').value=data['translated_text'];
            }
        });
    }
}

function load_destination_languages(){
    var text = document.getElementById('source-text').value;

    if (text.length > 0) {
        var source_language = document.getElementById('source-language').value;
        var url1 = "/api/languages/?source_language=" + source_language;
        $.ajax({
            url: url1,
            type: "GET",
            success: function(data) {
                const dest_language_select_tag = document.getElementById('target-language');

                for (let i=0;i<data['target_languages'].length;i++){
                    var option = document.createElement('option');

                    option.value = data['target_languages'][i]
                    option.text = data['target_languages'][i]

                    dest_language_select_tag.appendChild(option);
                }
            }
        });
    }
}

const user_textbox_tag = document.getElementById('source-text');

function update_text_length(){
    const user_text_count_tag = document.getElementById('count-text');
    var curr_len = user_textbox_tag.value.length;
    if (curr_len > 80){
        document.getElementById('text-length').classList.add("text-length-danger");
    }else{
        document.getElementById('text-length').classList.remove("text-length-danger");
    }
    user_text_count_tag.innerHTML = curr_len;
}

function detect_language(){
    if (user_textbox_tag.value.length) {
        $.ajax({
            url: "/api/detect_lang/",
            type: "POST",
            data: {
                text: user_textbox_tag.value,
                csrfmiddlewaretoken: csrf_token,
            },
            success: function(data) {
                document.getElementById('source-language').value = data['detectedLanguage'];
                load_destination_languages();
            }
        });
    }
}