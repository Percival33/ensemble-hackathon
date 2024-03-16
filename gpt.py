from openai import OpenAI


OPENAI_API_KEY = "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"

MODEL = "gpt-4"

PROMPT = """"""


def prompt_request(client: OpenAI, user_prompt, sys_prompt=None, model=MODEL) -> str:
    messages = []

    if sys_prompt:
        messages.append({"role": "system", "content": sys_prompt})

    messages.append({"role": "user", "content": user_prompt})

    response = client.chat.completions.create(
        messages=[messages],
        model=MODEL,
    )

    return response.choices[0].message.content


img1 = b'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAIAAAD8GO2jAAADPklEQVR4nH1WQZIkNwjMpNQ74dn1xb/2hxx+0fruCO9sT3eRPgASVdW2IqZHJSFACSTiH7//iRgk5pBigU7fiH0HacPwNvTjUwBAAFD+AUQ73YbGy+XcBGSCICMF36WPB2ODZ0lCaauvE7YcP26nIgESa4suetPOuCbbmcNxcxiMKm3d8vGTKi1e8mu3RAX6Fuqpwmzg6Qf0037tK8zNjYsoQChMEoKnWB4jBizOHE42kCuGMZFASGVnmVf9UADdJ06XIBPQ64xQXY0QQJVceiOCsgAsjBJQZZEAuBo0pZThu6c4QYFmIuigS4QQq2F1up7DUo+0P56+7zPYyhyXCHMQomAOQXKHN0cJlYXrsDn7+PEhkiSMAMiABBTDcZAAzct+ukAJlMzFWFQzRBrCSeD96y+DBhdc7R6kFAVBAcaWUiDBSum8TXg1bZCjIOP2dgOgltUR0Jh4nj/AkGGPcBOQZASRyYoW5BI/zlW1OsPWXCupAyA8VigAgxZ2agWQIZPW72VwkhwrJKlj4WjHE0Ub7OVbyub1XlR+eSOc4myhKyL1/Hkvz0mj2EIaZwm9YosXN6wli+wOteN2o2SbQU6jaZmbgBDlY6moIli02j0YmGTGpDLfneC+N5CkPDwnHZ++UFIHA+lgLDOzeH2WmpnBPRyNFVuCnahCkg+y9Q2eWxYg+XPH7jNnuVi0zp3TNirZ7P7z/v37Xz7bE00XOQCbmdEW9MFzDQ4RZwAlozC+3N6/fY2ryPB8fEaviOJcxW3UFpGcJX4YV7YTZJKPbfvt/Ve6SDzvj4+//yHt2sGzjNb69KL0B6M3IaroungFdG00yVEsVL1TZwfP+hOlSQEk6clFnL1pfLmN21ju1xuIgtsVldVMgejYCnhpGwhtHHMPUqPQUi4c2Bg4p5defQq+7yE94jp4qqEBUclKXKxENX3N68ul6jIAgAFSU0dXgTS9yE2Jh9qrYD46XsEXBpBUcqbPPHmg+wMDNROTQHR5OUUl4/75rMwKSmK9CYloi1m+c7n+FdVF3+VMNcvenlTxeOz/geUxF6+7yaPRuyPfBQi7Y3fE65rG929vmUj6/+f4CxvzXR3ZPKEORf8CuKD1MsLeGssAAAAASUVORK5CYII='


if __name__ == "__main__":
    client = OpenAI()

    response = client.chat.completions.create(
      model="gpt-4-vision-preview",
      messages=[
        {
          "role": "user",
          "content": [
            {"type": "text", "text": "From which ML dataset is this image?"},
            {
              "type": "image_url",
              "image_url": {
                "url": f"data:image/jpeg;base64,{base64_image}",
              },
            },
          ],
        }
      ],
      max_tokens=300,
    )

    print(response.choices[0])