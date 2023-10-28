
const Button = ({ children, onClick }) => {
  return (
    <button type="button" onClick={onClick} className="btn btn-primary">
      {children}
    </button>
  );
};

export default Button;
