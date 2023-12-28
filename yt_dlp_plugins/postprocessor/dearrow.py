from yt_dlp.postprocessor.common import PostProcessor

SUPPORTED_EXTRACTORS = {
    'Youtube',
}

class DeArrowPP(PostProcessor):
    def run(self, info):
        extractor = info['extractor_key']
        if extractor not in SUPPORTED_EXTRACTORS:
            self.to_screen(f'{self.PP_NAME} is not supported for {extractor}')
            return [], info

        # Call the DeArrow API
        api_data = self._download_json(
            f'https://sponsor.ajay.app/api/branding?videoID={info["id"]}') or {}

        # Check if titles are present in the API response
        if 'titles' in api_data and api_data['titles']:
            titles = [title.get('title') for title in api_data['titles'] if title.get('title')]

            # If multiple titles are found, let the user choose
            if len(titles) > 1:
                self.to_screen("Multiple titles found. Please choose one:")
                for i, title in enumerate(titles):
                    self.to_screen(f"{i + 1}: {title}")

                # Get user's choice
                choice = input("Enter the number of the title you want to choose: ")
                try:
                    # Validate user input
                    choice = int(choice) - 1
                    if choice < 0 or choice >= len(titles):
                        raise ValueError
                except ValueError:
                    self.to_screen("Invalid selection. Using the first title.")
                    choice = 0

                new_title = titles[choice]
            else:
                new_title = titles[0]

            # Store the original title and update with the new title
            info['original_title'] = info.get('title', '')
            self.to_screen(f'Original title: {info["original_title"]}')
            info['title'] = new_title

        else:
            self.to_screen("No new title found in the API response.")

        return [], info

