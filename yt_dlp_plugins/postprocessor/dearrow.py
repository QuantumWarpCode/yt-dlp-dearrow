from yt_dlp.postprocessor.common import PostProcessor

# Update this with the actual field mappings and API URL
DEARROW_FIELDS = {
    'title': 'dearrow_title',  # Example mapping
    # Add other fields as necessary
}
DEARROW_API_URL = 'https://sponsor.ajay.app/api/branding?videoID='  # Replace with actual API URL

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

        info['DEARROW'] = {
            'response': api_data,
            'original': {k: info.get(k) for k in DEARROW_FIELDS.keys()}
        }
        
        # RYD method
        #if api_data:
        #    info.update({k: api_data.get(v) for k, v in DEARROW_FIELDS.items()})

        info['title'] = info['DEARROW']['response']['titles'][0]['title']

        return [], info