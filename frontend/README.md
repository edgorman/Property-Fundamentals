# Property Fundamentals - Frontend
This is the [Node.js](https://nodejs.org/en/) and [React](https://reactjs.org/) frontend that hosts the web facing side of the project. This README assumes you have set up the developer environment as detailed in the base directory of this repository.

## Installation

To install the frontend:

```
npm install --prefix frontend
```

## Usage

To run the frontend in development mode:

```
npm start --prefix frontend
```

To build the frontend for production:

```
npm run build --prefix frontend
npm run serve --prefix frontend
```

## Testing

Run the testing scripts in the base directory:

```
npm run lint --prefix frontend
CI=true npm run test --prefix frontend
```
