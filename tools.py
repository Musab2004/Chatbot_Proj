tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get the current weather for a specific location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and state, e.g., San Francisco, CA",
                    }
                },
                "required": ["location"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "web_search",
            "description": "Use this function to perform any web search query.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The search query for the web search",
                    }
                },
                "required": ["query"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "create_video_json",
            "description": "Create JSON for a video with specified properties",
            "parameters": {
                "type": "object",
                "properties": {
                    "output_format": {
                        "type": "string",
                        "description": "The format of the output video, e.g., mp4",
                    },
                    "duration": {
                        "type": "string",
                        "description": "The duration of the video, e.g., 3 s",
                    },
                    "width": {
                        "type": "integer",
                        "description": "The width of the video, e.g., 1920",
                    },
                    "height": {
                        "type": "integer",
                        "description": "The height of the video, e.g., 1080",
                    },
                    "elements": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "type": {
                                    "type": "string",
                                    "description": "The type of the element, e.g., text",
                                },
                                "track": {
                                    "type": "integer",
                                    "description": "The track number of the element, e.g., 1",
                                },
                                "time": {
                                    "type": "string",
                                    "description": "The start time of the element, e.g., 0 s",
                                },
                                "duration": {
                                    "type": "string",
                                    "description": "The duration of the element, e.g., 1 s",
                                },
                                "fill_color": {
                                    "type": "string",
                                    "description": "The fill color of the element, e.g., #ffffff",
                                },
                                "text": {
                                    "type": "string",
                                    "description": "The text content of the element",
                                },
                                "font_family": {
                                    "type": "string",
                                    "description": "The font family of the text, e.g., Open Sans",
                                },
                            },
                            "required": [
                                "type",
                                "track",
                                "time",
                                "duration",
                                "fill_color",
                                "text",
                                "font_family",
                            ],
                        },
                    },
                },
                "required": [
                    "output_format",
                    "duration",
                    "width",
                    "height",
                    "elements",
                ],
            },
        },
    },
]
