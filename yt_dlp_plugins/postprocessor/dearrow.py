from yt_dlp.postprocessor.common import PostProcessor

SUPPORTED_EXTRACTORS = {
    'Youtube',
}

class DeArrowPP(PostProcessor):
    def __init__(self, downloader=None, **kwargs):
        super().__init__(downloader)
        self._kwargs = kwargs
        self.select_title = kwargs.get('SelectTitle', "False") == "True"
    
    def run(self, info):
        extractor = info['extractor_key']
        # self.to_screen(f'Received kwargs:  :) {self._kwargs}')
        # self.to_screen(f'select_title is set to: {self.select_title}')

        if extractor not in SUPPORTED_EXTRACTORS:
            self.to_screen(f'{self.PP_NAME} is not supported for {extractor}')
            return [], info

        # Call the DeArrow API
        api_data = self._download_json(
            f'https://sponsor.ajay.app/api/branding?videoID={info["id"]}') or {}

        if 'titles' not in api_data or not api_data['titles']:
            self.to_screen("No new title found in the API response.")
            return [], info

        titles = [title.get('title') for title in api_data['titles'] if title.get('title')]

        if len(titles) <= 1 or not self.select_title:
            new_title = titles[0]
        else:
            self.to_screen("Multiple titles found. Please choose one:")
            for i, title in enumerate(titles):
                self.to_screen(f"{i + 1}: {title}")

            choice = input("Enter the number of the title you want to choose: ")
            try:
                choice = int(choice) - 1
                if choice < 0 or choice >= len(titles):
                    raise ValueError
            except ValueError:
                self.to_screen("Invalid selection. Using the first title.")
                choice = 0

            new_title = titles[choice]

        # Store the original title and update with the new title
        info['original_title'] = info.get('title', '')
        self.to_screen(f'Original title: {info["original_title"]}')
        info['title'] = new_title

        return [], info
