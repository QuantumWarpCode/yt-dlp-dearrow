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

        # Store the original title
        info['original_title'] = info.get('title', '')
        info['dearrow_title'] = 'NA'
        
        # Check if the title is present in the API response and update accordingly
        if 'titles' in api_data and api_data['titles']:
            new_title = api_data['titles'][0].get('title')
            if new_title:
                self.to_screen(f'Original title: {info["original_title"]}')

                # Update the title
                info['title'] = new_title
                info['dearrow_title'] = new_title
        else:
            self.to_screen("No new title found in the API response.")
            # print(api_data)     

        return [], info
