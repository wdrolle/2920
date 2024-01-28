import React, { useState, useEffect, useContext, useCallback } from 'react';
import { styled, Box, TextareaAutosize, Button, InputBase, FormControl } from '@mui/material';
import { AddCircle as Add } from '@mui/icons-material';
import { useNavigate, useLocation } from 'react-router-dom';
import { API } from '../../service/api';
import { DataContext } from '../../context/DataProvider';

const Container = styled(Box)(({ theme }) => ({
    margin: '50px 100px',
    [theme.breakpoints.down('md')]: {
        margin: 0
    }
}));

const Image = styled('img')({
    width: '100%',
    height: '50vh',
    objectFit: 'cover'
});

const StyledFormControl = styled(FormControl)`
    margin-top: 10px;
    display: flex;
    flex-direction: row;
`;

const InputTextField = styled(InputBase)`
    flex: 1;
    margin: 0 30px;
    font-size: 25px;
`;

const Textarea = styled(TextareaAutosize)`
    width: 100%;
    border: none;
    margin-top: 50px;
    font-size: 18px;
    &:focus-visible {
        outline: none;
    }
`;

const initialPost = {
    title: '',
    description: '',
    picture: '',
    username: '',
    categories: '',
    createdDate: new Date()
};

const CreatePost = () => {
    const navigate = useNavigate();
    const location = useLocation();

    const [post, setPost] = useState(initialPost);
    const [file, setFile] = useState('');
    const [error, setError] = useState(null); // Error state for handling API and file upload errors
    const { account } = useContext(DataContext);

    // Function to handle image upload
    const uploadImage = useCallback(async () => {
        try {
            if (file) {
                const data = new FormData();
                data.append("name", file.name);
                data.append("file", file);

                const response = await API.uploadFile(data);
                setPost({ ...post, picture: response.data }); // Update the post state with the image URL
            }
        } catch (error) {
            setError("Error uploading image. Please try again."); // Handle upload error
        }
    }, [file, post, setPost]);

    // Effect to upload image and set post properties
    useEffect(() => {
        const uploadAndSetImage = async () => {
            await uploadImage(); // Make sure the image upload is complete
            post.categories = location.search?.split('=')[1] || 'All';
            post.username = account.username;
            setPost({ ...post }); // Trigger a re-render to update the post state
        };

        uploadAndSetImage();
    }, [file, location.search, account.username, post, uploadImage]);

    // Function to save the post
    const savePost = async () => {
        try {
            await API.createPost(post);
            navigate('/');
        } catch (error) {
            setError("Error creating the post. Please try again."); // Handle API request error
        }
    };

    // Function to handle form input changes
    const handleChange = (e) => {
        setPost({ ...post, [e.target.name]: e.target.value });
    };

    return (
        <Container>
            <Image src={post.picture || 'url-of-default-image.jpg'} alt="post" />

            <StyledFormControl>
                <label htmlFor="fileInput">
                    <Add fontSize="large" color="action" />
                </label>
                <input
                    type="file"
                    id="fileInput"
                    style={{ display: "none" }}
                    onChange={(e) => setFile(e.target.files[0])}
                />
                <InputTextField onChange={(e) => handleChange(e)} name='title' placeholder="Title" />
                <Button onClick={() => savePost()} variant="contained" color="primary">Publish</Button>
            </StyledFormControl>

            <Textarea
                rowsMin={5}
                placeholder="Tell your story..."
                name='description'
                onChange={(e) => handleChange(e)}
            />

            {error && <p style={{ color: 'red' }}>{error}</p>} {/* Display error message if there's an error */}
        </Container>
    )
};

export default CreatePost;
