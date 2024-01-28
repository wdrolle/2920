import { AppBar, Toolbar, styled, Button } from '@mui/material'; 
import { Link } from 'react-router-dom';

import { useNavigate } from 'react-router-dom';


const Component = styled(AppBar)`
    background: #FFFFFF;
    color: black;
`;

const Container = styled(Toolbar)`
    justify-content: center;
    & > a {
        padding: 20px;
        color: #000;
        text-decoration: none;
    }
`

const Header = () => {
    const navigate = useNavigate();

    const logout = async () => {
        try {
            // Perform logout logic here, e.g., clearing session or state
            // Example: Clearing user session token and user data
            // await clearSession(); // You should implement this function
            
            // After logout, navigate to the desired page, e.g., '/account'
            navigate('/account');
        } catch (error) {
            // Handle any errors that occur during logout
            console.error('Logout error:', error);
        }
    }

    return (
        <Component>
            <Container>
                <Link to='/'>HOME</Link>
                <Link to='/about'>ABOUT</Link>
                <Link to='/contact'>CONTACT</Link>
                <Button onClick={logout}>LOGOUT</Button> {/* Logout button */}
            </Container>
        </Component>
    )
}

export default Header;