

let app = new Vue({
    el: '#app',
    data: {
        rotx_offset: '',
        text_to_encode: '',
        encoded_text: ''
    },
    methods: {
        encodeText: function() {

            if (this.text_to_encode === '' || this.rotx_offset === '') {
                // alert('Please fill out all fields')
                div_alert.style.display = ''
                setTimeout(function() {
                    div_alert.style.display = 'none'
                }, 3000)
                return
            }

            encoded_group.style.display = 'block'

            //encoded_group.style.display = ''
            console.log("text_to_encode: " + this.text_to_encode)
            console.log("rotx_offset: " + this.rotx_offset)
            this.encoded_text = rotx(this.text_to_encode, this.rotx_offset)
        },
        hideRotx: function() {
            encoded_group.style.display = 'none'
        },
        copyText: function() {
            //document.execCommand("copy");
            //alert("Copied the text: " + this.encoded_text);
            navigator.clipboard.writeText(this.encoded_text).then(function() {
                console.log('Copying to clipboard was successful! ' + this.encoded_text)
              }, function(err) {
                console.error('Could not copy text: ', err)
              })
        }
    }
})


// ROT encoder with a larger character set which supports all ASCII characters and punctation
function rotx(text, offset) {

    const alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~0123456789 \t\n'
    offset = parseInt(offset)
    // Compenstate for large negative numbers
    if (offset < (-1 * alphabet.length)) {
        offset = offset * -1
    }

    if (offset < 0) { // Compenstate for negative numbers
        offset += alphabet.length
    } else if (offset > alphabet.length) { // Compenstate for large numbers
        offset %= alphabet.length
    }

    console.log("Offset: " + offset)
    let output = ''
    for (let i=0; i<text.length; i++) {
        let char = text[i]
        console.log("char: " + char)
        let alphabet_index = alphabet.indexOf(char)
        console.log("index of char: " + alphabet_index)
        if (alphabet_index == -1) {
            output += char
        } else {
            alphabet_index += offset
            console.log("alphabet_index: " + alphabet_index)
            alphabet_index %= alphabet.length
            console.log("alphabet_index after mod: " + alphabet_index)
            output += alphabet[alphabet_index]
        }
    }
    console.log("Output: " + output)
    return output
}










/* 
function copyToClipboard(text, el) {
    var copyTest = document.queryCommandSupported('copy');
    var elOriginalText = el.attr('data-original-title');
  
    if (copyTest === true) {
      var copyTextArea = document.createElement("textarea");
      copyTextArea.value = text;
      document.body.appendChild(copyTextArea);
      copyTextArea.select();
      try {
        var successful = document.execCommand('copy');
        var msg = successful ? 'Copied!' : 'Whoops, not copied!';
        el.attr('data-original-title', msg).tooltip('show');
      } catch (err) {
        console.log('Oops, unable to copy');
      }
      document.body.removeChild(copyTextArea);
      el.attr('data-original-title', elOriginalText);
    } else {
      // Fallback if browser doesn't support .execCommand('copy')
      window.prompt("Copy to clipboard: Ctrl+C or Command+C, Enter", text);
    }
  }
  
  $(document).ready(function() {
    // Initialize
    // ---------------------------------------------------------------------
  
    // Tooltips
    // Requires Bootstrap 3 for functionality
    $('.js-tooltip').tooltip();
  
    // Copy to clipboard
    // Grab any text in the attribute 'data-copy' and pass it to the 
    // copy function
    $('.js-copy').click(function() {
      var text = $(this).attr('data-copy');
      var el = $(this);
      copyToClipboard(text, el);
    });
  });  

       <div class="contact">
            <div class="btn-group">
                <a class="btn btn-primary">{{ encoded_text }}</a>
                <button type="button" class="btn btn-default btn-copy js-tooltip js-copy" data-toggle="tooltip"
                    data-placement="bottom" data-copy="encoded_text" title="Copy to clipboard">
                    <!-- icon from google's material design library -->
                    <svg class="icon" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
                        version="1.1" width="24" height="24" viewBox="0 0 24 24">
                        <path
                            d="M17,9H7V7H17M17,13H7V11H17M14,17H7V15H14M12,3A1,1 0 0,1 13,4A1,1 0 0,1 12,5A1,1 0 0,1 11,4A1,1 0 0,1 12,3M19,3H14.82C14.4,1.84 13.3,1 12,1C10.7,1 9.6,1.84 9.18,3H5A2,2 0 0,0 3,5V19A2,2 0 0,0 5,21H19A2,2 0 0,0 21,19V5A2,2 0 0,0 19,3Z" />
                    </svg>
                </button>
            </div>
        </div>
    */
